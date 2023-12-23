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

#### Backend

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `app.py` | home | Controller of the app. The main file which executes the app. |
| `db.py`  | config  | Creates the connection to the database. |
| `setup_mysql.sql` | database   | Creates the database and the user. |
| `affinity_data_structuring.py` | etl | Structures the connections data to fit the database table. |
| `investors_data_structuring.py` | etl | Structures the investors data to fit the database table. |
| `consolidate.py` | models | Creates the investors and connections tables in SQLAlchemy. |
| `insert_investors_db.py` | models | Inserts the investors data into the database. |
| `insert_connections.py` | models | Inserts the connections data into the database. |
| `consolidated_routes.py` | routes  | Defines the CRUD for the investors in the API. |
| `connection_routes.py` | routes |  Defines the CRUD for the connections in the API. |
| `investors.py` | schemas  | Defines the schema for an investors object for the API. |
| `connections.py` | schemas | Defines the schema for an connections object for the API. |

#### Frontend

| File  | Directory  | Description |
| :------ |:--------------| :---------------------|
| `index.html` | public | Base HTML file of the DOM. |
| `App.js` | src | Controller file for the components. |
| `index.js` | src | Creates all the react components based on id in HTML. |
| `table.js` | src | File that contains the table and the filters. |
| `/components` | src | Directory that contains the individual components. |
| `/style` | src  | Directory that contains the CSS files and pictures. |

## How to Install and Run the Project

In order to install and run the project, you first need to clone the repository. Then, you need to create a Python Virtual Environment with the command `venv <name of the environment>`. Activate the virtual environment with the command `source <name of the environment>/bin/activate`. Then you need to install the requirements with the command `pip install -r requirements.txt`. Finally you need to get inside the front directoy and install the react dependencies with the command `npm install`.

Once you have installed all the dependencies, you need to create the database and the user executing the file `set_up.sql` with the command `cat database/setup_mysql.sql | mysql`. Then you need to create the tables with the command `python models/consolidate.py`. Finally, you need to insert the data executing the following commands in order, `python models/insert_investors_db.py` and then `python models/insert_connections.py`. This process has to be done only the first time you are installing the project.

You first need to get into the home directoy and run the command `uvicorn app:app` to run the API. Finally, get inside the front directory in another terminal and run the command `npm start` to run the front. 

## How to Use the Project

![Untitled-video-Made-with-Clipchamp](https://user-images.githubusercontent.com/106627368/220689993-80017813-878e-4beb-98b7-7e72aa8ff39f.gif)


## Author

<a href = 'https://www.twitter.com'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a> [@Alejandro García](https://twitter.com/dagarciaz?t=SsP1iYjxXsK7z9nBZxwSvQ&s=08) | [@Juan Esteban Hernandez](https://twitter.com/0110Juanes?t=zVQP_NQVayj4JzjPc0OdQQ&s=09) | [@Juan David Otálora](https://twitter.com/juandotalora)
