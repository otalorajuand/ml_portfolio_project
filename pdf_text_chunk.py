import os
import PyPDF2


# Function to chunk text
def chunk_text(text, chunk_size):
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

# Function to extract text from PDF and chunk it
def extract_and_chunk_text(file_path):
    chunks_info = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            # Split text into chunks approximately the size of a page
            chunks = chunk_text(text, 2000)  # Adjust the chunk size as needed
            chunks_info.extend(chunks)
    return chunks_info

# Function to process directory
def process_directory(directory_path):
    files_list = []
    unique_id = 1
    min_chunk_size = 100
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            chunks_info = extract_and_chunk_text(file_path)
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

# Replace 'path_to_your_directory' with the path to your directory containing PDF files
directory_path = '/Users/otalorajuand/Desktop/data-santuario'

data_dict = process_directory(directory_path)



