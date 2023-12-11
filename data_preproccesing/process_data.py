from embedding import embedding_dict_to_dataframe
from create_data_dict import process_directory
import yaml
"""Extracts data from pdfs and create jsonl"""

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

directory_path = config['directory_path']
max_chunk_size = config['max_chunk_size']
min_chunk_size = config['min_chunk_size']


if __name__ == "__main__":

    data_dict = process_directory(directory_path,
                                  max_chunk_size,
                                  min_chunk_size)
    embedding_dict_to_dataframe(data_dict)
