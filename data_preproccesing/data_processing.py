import os
import PyPDF2
import requests
import pandas as pd
import torch
from dotenv import load_dotenv
import yaml


class DataProcessing:
    """Handles data processing operations including PDF text extraction,
      chunking, and embeddings"""

    def __init__(self, config_path='config.yml'):
        load_dotenv()
        self.hf_token = os.getenv('HF_TOKEN')
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.model_name = self.config['model_name']
        self.api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{self.model_name}"
        self.headers = {"Authorization": f"Bearer {self.hf_token}"}

    @staticmethod
    def chunk_text(text, chunk_size):
        """Splits the input text into chunks based on the specified chunk size.

        Args:
        - text (str): The input text to be chunked.
        - chunk_size (int): The maximum size of each chunk in terms of characters.

        Returns:
        - chunks (list): A list of chunks where each chunk is a string not
        exceeding the chunk size.
        """
        chunks = []
        words = text.split()
        current_chunk = ''
        for word in words:
            if len(current_chunk) + len(word) + 1 <= chunk_size:
                current_chunk += word + ' '
            else:
                chunks.append(current_chunk)
                current_chunk = word + ' '
        if current_chunk:
            chunks.append(current_chunk)
        return chunks

    def extract_and_chunk_text(self, file_path, chunk_size):
        """Extracts text from a PDF file, chunks it based on a specified size,
        and returns information about the text chunks.

        Args:
        - file_path (str): The path to the PDF file.
        - chunk_size (int): The desired size (approximate) for each text chunk.

        Returns:
        - A list containing information about text chunks extracted from the PDF.
        Each element in the list represents a chunk and its associated
        information.
        """

        chunks_info = []
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                # Split text into chunks approximately the size of a page
                chunks = self.chunk_text(text, chunk_size)
                chunks_info.extend(chunks)
        return chunks_info

    def process_directory(self, directory_path, chunk_size, min_chunk_size):
        """Process directory and extract information from PDF files.

        Args:
        - directory_path (str): Path to the directory containing PDF files.
        - chunk_size (int): Maximum size for text chunking.
        - min_chunk_size (int): Minimum size of text chunk to be considered.

        Returns:
        - files_list (list): A list of dictionaries containing information
        extracted from PDF files. Each dictionary includes 'id', 'title',
        and 'text_chunk' for each valid chunk found.
        """

        files_list = []
        unique_id = 1
        for filename in os.listdir(directory_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(directory_path, filename)
                chunks_info = self.extract_and_chunk_text(
                    file_path, chunk_size)
                for chunk_text in chunks_info:

                    file_info = {
                        'id': unique_id,
                        'title': filename,
                        'text_chunk': chunk_text
                    }
                    if len(chunk_text) > min_chunk_size:
                        files_list.append(file_info)
                        unique_id += 1
        return files_list

    def query(self, texts):
        """Queries the Hugging Face API for feature extraction.

        Args:
        - texts: a list of texts to be processed

        Returns: JSON response containing extracted features
        """

        response = requests.post(
            self.api_url, headers=self.headers, json={
                "inputs": texts, "options": {
                    "wait_for_model": True}})
        return response.json()

    def embedding_dict_to_dataframe(self, data_dict):
        """Processes embedding data from a dictionary and saves it into a CSV file.

        Args:
        - data_dict: a dictionary containing embedding data

        Saves the processed data into a 'train.csv' file.
        """

        data = pd.DataFrame.from_records(data_dict)
        data['new_column'] = data.title + ' - ' + data.text_chunk.str.lower()

        texts = list(data.new_column)

        output_list = []
        step = 50
        for i in range(0, len(texts), step):
            current_slice = texts[i:i + step]

            print(f"Processing slice {i // step + 1}:")
            output = self.query(current_slice)
            output_list.extend(output)

        output = self.query(texts)

        embeddings = pd.DataFrame(output)

        dataset_embeddings = torch.from_numpy(
            embeddings.to_numpy()).to(
            torch.float)

        data_2 = pd.DataFrame(data=dataset_embeddings.numpy())

        df_3 = pd.concat([data, data_2], axis=1)

        df_3.to_csv("train.csv", index=False)

    def execute_data_processing(self):
        # Executes data processing operations
        directory_path = self.config['directory_path']
        max_chunk_size = self.config['max_chunk_size']
        min_chunk_size = self.config['min_chunk_size']

        data_dict = self.process_directory(
            directory_path, max_chunk_size, min_chunk_size)
        self.embedding_dict_to_dataframe(data_dict)
