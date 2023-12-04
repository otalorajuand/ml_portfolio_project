from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

repo_id = "tiiuae/falcon-7b-instruct"

llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(question))