import os
import PyPDF2


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


def extract_and_chunk_text(file_path, chunk_size):
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
            # Adjust the chunk size as needed
            chunks = chunk_text(text, chunk_size)
            chunks_info.extend(chunks)
    return chunks_info

# Function to process directory


def process_directory(directory_path, chunk_size, min_chunk_size):
    """Process files in a directory, extract text, and create text chunks.

    Args:
    - directory_path (str): Path to the directory containing files.
    - chunk_size (int): Maximum size of each text chunk.
    - min_chunk_size (int): Minimum size of text required to create a chunk.

    Returns:
    - list: A list of dictionaries containing information about text chunks
      extracted from files.
      Each dictionary contains:
        - 'id' (int): Unique identifier for the text chunk.
        - 'title' (str): Title or filename of the file the chunk was extracted
           from.
        - 'text_chunk' (str): Extracted text chunk.
    """
    files_list = []
    unique_id = 1
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            chunks_info = extract_and_chunk_text(file_path, chunk_size)
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
