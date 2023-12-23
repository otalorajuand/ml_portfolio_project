# Retrieval Augmented Generation (RAG) System for Question Answering for The House Museum El Santuario

![Contributors](https://img.shields.io/github/contributors/otalorajuand/ml_portfolio_project?style=plastic)
![Forks](https://img.shields.io/github/forks/otalorajuand/ml_portfolio_project)
![Stars](https://img.shields.io/github/stars/otalorajuand/ml_portfolio_project)
![Licence](https://img.shields.io/github/license/otalorajuand/ml_portfolio_project)
![Issues](https://img.shields.io/github/issues/otalorajuand/ml_portfolio_project)
![Languages](https://img.shields.io/github/languages/count/otalorajuand/ml_portfolio_project)

## Description

This project addresses a specific need identified at the House Museum El Santuario—a foundation dedicated to fostering cultural and educational development in El Santuario, Colombia. The primary challenge was to consolidate historical town information and administrative data within the institution. To tackle this, I devised a chat-based solution enabling users to query both these topics, receiving AI-generated responses leveraging the museum's accumulated information.

The solution implemented here is a Retrieval Augmented Generation (RAG) system. Initially, I curated significant historical documents about the town's history and the institution's administrative records. Subsequently, I processed this wealth of information by segmenting it into smaller data chunks and converting it to lowercase. These segmented data chunks were then embedded into a vector space. Whenever a user submits a query, the system embeds the question into the same vector space, selects the k most relevant chunks, and supplies them as context to a Large Language Model (LLM). This contextualized information enables the LLM to craft accurate responses.

One of the distinguishing features of this project is its modularized codebase, allowing for seamless switching between embedding and LM methods. I utilized the Hugging Face inference API for embedding tasks and the OpenAI ChatGPT3.5 Turbo for the LLM aspect. For the user interface, Streamlit was employed, simplifying the remote deployment of the entire project.



## Diagrams and Flow Chart

![higher_level](https://user-images.githubusercontent.com/22607461/218857148-9e2e8025-ff18-408a-b8f7-93c5c3cd9825.jpeg)
![medium-level](https://user-images.githubusercontent.com/22607461/218857302-9073a781-60f7-4f6c-88a0-07846c71f6af.jpeg)
![diagrama_de_archivos](https://user-images.githubusercontent.com/22607461/219759319-dee60c42-4da5-49e4-bd45-e5d98e29acde.jpeg)

### Files

### App

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `Hello.py` | root |  |
| `1_Data_Museo.py` | root |  |
| `2_Data_Santuario.py` | root |  |


#### Prompt Generation

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `augmented_prompt.py` | prompt_generation | Defines the class AugmentedPrompt which generates the context-based augmented prompt and associated document information to answer queries. |
| `llm.py`  | prompt_generation  | Defines the class 'Llm' which enables output generation based on provided prompts using specified LLM model parameters. |
| `query.py` | prompt_generation   | Defines the class 'Query' which generates embeddings for a provided query." |
| `source_knowledge.py` | prompt_generation | Defines a Python class SourceKnowledge that models the source knowledge for feeding augmented prompts. It facilitates dataset loading, generates embeddings from input data, and retrieves relevant knowledge based on a specified query using Semantic Search, presenting it as concatenated text results and a bullet-pointed list of unique document titles extracted from a specified dataset. |


#### Data Preprocessing

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `create_data_dict.py` | data_preproccesing |  |
| `embedding.py` | data_preproccesing |  |
| `pdf_text_chunk.py` | data_preproccesing |  |
| `process_data.py` | data_preproccesing |  |

## How to Install and Run the Project

In order to install and run the project, you first need to clone the repository. Then, you need to create a Python Virtual Environment with the command `venv <name of the environment>`. Activate the virtual environment with the command `source <name of the environment>/bin/activate`. Then you need to install the requirements with the command `pip install -r requirements.txt`. Finally you need to get inside the front directoy and install the react dependencies with the command `npm install`.

Once you have installed all the dependencies, you need to create the database and the user executing the file `set_up.sql` with the command `cat database/setup_mysql.sql | mysql`. Then you need to create the tables with the command `python models/consolidate.py`. Finally, you need to insert the data executing the following commands in order, `python models/insert_investors_db.py` and then `python models/insert_connections.py`. This process has to be done only the first time you are installing the project.

You first need to get into the home directoy and run the command `uvicorn app:app` to run the API. Finally, get inside the front directory in another terminal and run the command `npm start` to run the front. 

## How to Use the Project

![Untitled-video-Made-with-Clipchamp](https://user-images.githubusercontent.com/106627368/220689993-80017813-878e-4beb-98b7-7e72aa8ff39f.gif)


## Author

<a href = 'https://www.github.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>  [@Juan David Otálora](https://github.com/otalorajuand)

<a href = 'https://www.twitter.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a>  [@Juan David Otálora](https://twitter.com/juandotalora)

<a href = 'https://www.linkedin.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg"/></a> [@Juan David Otálora](https://www.linkedin.com/in/juan-david-ot%C3%A1lora-carrillo-7a6599172/)
