from datasets import load_dataset
import streamlit as st
from sentence_transformers.util import semantic_search
import torch


@st.cache_data(show_spinner="Inicializando aplicación")
def load_data():

    data_url = 'otalorajuand/data_house_museum'
    dataset = load_dataset(
        data_url,
        split="train").to_pandas()
    return dataset 

@st.cache_data
def dataset_embbedings_generator(dataset):

    not_embedding_columns = ['id', 'title', 'text_chunk', 'new_column']
    embeddings = dataset.drop(columns=not_embedding_columns)

    embeddings_dataset = torch.from_numpy(embeddings.to_numpy()).to(torch.float)

    return embeddings_dataset

def source_knowledge_generator(embedded_query, embeddings_dataset, top_k, dataset):

    # source_knowledge generation
    query_embeddings = torch.FloatTensor(embedded_query)
    hits = semantic_search(query_embeddings, embeddings_dataset, top_k=top_k)
    selected_rows = [hits[0][i]['corpus_id'] for i in range(len(hits[0]))]
    results = dataset.loc[selected_rows, [
        'new_column']].values.tolist()
    documents = dataset.loc[selected_rows, [
        'title']].values.tolist()
    # get the text from the results
    source_knowledge = "\n".join([x[0] for x in results])

    return source_knowledge, documents