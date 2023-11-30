import os
from pdf_text_chunk import extract_and_chunk_text
"""Creates the data dictionary"""



def process_directory(directory_path, chunk_size, min_chunk_size):
    """Function to process directory"""
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