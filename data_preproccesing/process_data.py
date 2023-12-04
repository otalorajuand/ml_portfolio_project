from embedding import embedding_dict_to_dataframe
from create_data_dict import process_directory
"""Extracts data from pdfs and create jsonl"""

directory_path = '/Users/otalorajuand/Desktop/data-santuario'
max_chunk_size = 2000
min_chunk_size = 100

if __name__ == "__main__":

    data_dict = process_directory(directory_path,
                                  max_chunk_size, 
                                  min_chunk_size)
    embedding_dict_to_dataframe(data_dict)
