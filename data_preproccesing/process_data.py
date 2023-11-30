from create_jsonl import create_json
from pdf_text_chunk import process_directory, extract_and_chunk_text
"""Extracts data from pdfs and create jsonl"""

directory_path = '/home/ml_portofolio_project/data_preproccesing'
chunk_size = 2000
min_chunk_size = 100

if __name__ == "__main__":

    data_dict = process_directory(directory_path, chunk_size, min_chunk_size)
    create_json(data_dict)
