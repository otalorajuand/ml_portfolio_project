# Retrieval Augmented Generation (RAG) System for Question Answering for The House Museum El Santuario

![GitHub contributors](https://img.shields.io/github/contributors/otalorajuand/ml_portfolio_project)
![GitHub forks](https://img.shields.io/github/forks/otalorajuand/ml_portfolio_project)
![Stars](https://img.shields.io/github/stars/otalorajuand/ml_portfolio_project)
![Licence](https://img.shields.io/github/license/otalorajuand/ml_portfolio_project)
![Issues](https://img.shields.io/github/issues/otalorajuand/ml_portfolio_project)
![Languages](https://img.shields.io/github/languages/count/otalorajuand/ml_portfolio_project)

## Description

This project addresses a specific need identified at the House Museum El Santuario—a foundation dedicated to fostering cultural and educational development in El Santuario, Colombia. The primary challenge was to consolidate historical town information and administrative data within the institution. To tackle this, I devised a chat-based solution enabling users to query both these topics, receiving AI-generated responses leveraging the museum's accumulated information.

The solution implemented here is a Retrieval Augmented Generation (RAG) system. Initially, I curated significant historical documents about the town's history and the institution's administrative records. Subsequently, I processed this wealth of information by segmenting it into smaller data chunks and converting it to lowercase. These segmented data chunks were then embedded into a vector space. Whenever a user submits a query, the system embeds the question into the same vector space, selects the k most relevant chunks, and supplies them as context to a Large Language Model (LLM). This contextualized information enables the LLM to craft accurate responses.

One of the distinguishing features of this project is its modularized codebase, allowing for seamless switching between embedding and LM methods. I utilized the Hugging Face inference API for embedding tasks and the OpenAI ChatGPT3.5 Turbo for the LLM aspect. For the user interface, Streamlit was employed, simplifying the remote deployment of the entire project.



## Diagrams and Flow Chart

![diagrama_1](https://github.com/otalorajuand/ml_portfolio_project/assets/22607461/6f2eaeaa-ce6e-4a07-a834-09495397884a)
![llm_diagram](https://github.com/otalorajuand/ml_portfolio_project/assets/22607461/f4850c7e-b9c2-4413-a75f-fe69081d4efb)
![rag_diagram](https://github.com/otalorajuand/ml_portfolio_project/assets/22607461/8ed88a70-5376-45b5-8a2d-72e754831fb0)

### Files

### App

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `Home.py` | root | Main file to execute the app. |
| `1_Casa_Museo.py` | pages | Page containing the chat for questions related to the museum. |
| `2_Historia_Santuario.py` | pages | Page containing the chat for questions related to the town's history. |


#### Prompt Generation

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `augmented_prompt.py` | prompt_generation | Defines the class AugmentedPrompt which generates the context-based augmented prompt and associated document information to answer queries. |
| `llm.py`  | prompt_generation  | Defines the class 'Llm' which enables output generation based on provided prompts using specified LLM model parameters. |
| `query.py` | prompt_generation | Defines the class 'Query' which generates embeddings for a provided query." |
| `source_knowledge.py` | prompt_generation | Defines a Python class 'SourceKnowledge' that models the source knowledge for feeding augmented prompts. It facilitates dataset loading, generates embeddings from input data, and retrieves relevant knowledge based on a specified query using Semantic Search, presenting it as concatenated text results and a bullet-pointed list of unique document titles extracted from a specified dataset. |


#### Data Preprocessing

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `data_processing.py` | data_preproccesing | Defines the class 'DataProcessing' which extracts, tranforms and exports a csv file with the data to feed the database. |
| `process_data.py` | data_preproccesing | The main file that executes the data preprocessing. |

## How to Install and Run the Project

In order to install and run the project, you first need to clone the repository. Then, you need to create a Python Virtual Environment with the command `venv <name of the environment>`. Activate the virtual environment with the command `source <name of the environment>/bin/activate`. Then you need to install the requirements with the command `pip install -r requirements.txt`.

Once you have installed all the dependencies, you need to create the database and upload the file into the huggingface hub. In order to run the main file for the data preprocessing you need to run the following command `python3 data_preproccesing/data_processing.py`. Once the csv file is created, you need to upload it the hf hub. 

Then, you can run the app with the command `streamlit run app.py` and a new window will open with it. You can also deploy it using the streamlit cloud service.s

## How to Use the Project

![ezgif com-video-to-gif-converter](https://github.com/otalorajuand/ml_portfolio_project/assets/22607461/5bdfe613-0ec3-4ef2-8047-7de20db55f9e)



## Author

<a href = 'https://www.github.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>  [@Juan David Otálora](https://github.com/otalorajuand)

<a href = 'https://www.twitter.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a>  [@Juan David Otálora](https://twitter.com/juandotalora)

<a href = 'https://www.linkedin.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg"/></a> [@Juan David Otálora](https://www.linkedin.com/in/juan-david-ot%C3%A1lora-carrillo-7a6599172/)
