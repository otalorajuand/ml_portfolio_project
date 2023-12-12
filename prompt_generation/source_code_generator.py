from datasets import load_dataset
import streamlit as st
from sentence_transformers.util import semantic_search
import torch
import yaml

with open('prompt_generation/config.yml', 'r') as file:
    config = yaml.safe_load(file)

@st.cache_data(show_spinner="Inicializando aplicación")
def load_data():
    """Loads and returns a dataset from a specified data URL using
       Hugging Face's datasets library.

    Returns:
    - dataset: a Pandas DataFrame containing the loaded dataset
    """

    data_url = config['data_url']
    dataset = load_dataset(
        data_url,
        split="train").to_pandas()
    return dataset


@st.cache_data
def dataset_embbedings_generator(dataset):
    """Generates embeddings dataset from the input dataset.

    Args:
    - dataset: Pandas DataFrame containing the dataset for embedding generation.

    Returns:
    - embeddings_dataset: Torch Tensor representing the embeddings dataset
                          derived from the input dataset after dropping
                          specific columns.
    """

    not_embedding_columns = ['id', 'title', 'text_chunk', 'new_column']
    embeddings = dataset.drop(columns=not_embedding_columns)

    embeddings_dataset = torch.from_numpy(
        embeddings.to_numpy()).to(torch.float)

    return embeddings_dataset


def source_knowledge_generator(embedded_query,
                               embeddings_dataset,
                               top_k,
                               dataset):
    """
    Generates source knowledge and a list of unique documents related to a
    given query.

    Args:
    - embedded_query: Torch tensor or array containing embeddings of the query
    - embeddings_dataset: Torch tensor or array containing embeddings of the
                          dataset
    - top_k: Integer specifying the top-k results to retrieve
    - dataset: Pandas DataFrame containing the dataset with columns
               'new_column' and 'title'

    Returns:
    - source_knowledge: String containing concatenated results from
                        'new_column' based on the retrieved top-k indices
    - documents_list: String containing a bullet-pointed list of unique
                      document titles extracted from 'title' column
    """

    # source_knowledge generation
    print(embedded_query)
    st.write(embedded_query)
    query_embeddings = torch.FloatTensor(embedded_query)
    hits = semantic_search(query_embeddings, embeddings_dataset, top_k=top_k)
    selected_rows = [hits[0][i]['corpus_id'] for i in range(len(hits[0]))]
    results = dataset.loc[selected_rows, [
        'new_column']].values.tolist()
    documents = dataset.loc[selected_rows, [
        'title']].values.tolist()
    # get the text from the results
    source_knowledge = "\n".join([x[0] for x in results])

    unique_documents = list(set([x[0].replace(".pdf", "") for x in documents]))
    documents_list = "\n".join([f"• {item}" for item in unique_documents])

    return source_knowledge, documents_list
