import os
from pdf_text_chunk import extract_and_chunk_text
"""Creates the data dictionary"""


def process_directory(directory_path, chunk_size, min_chunk_size):
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
