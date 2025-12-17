from langchain_classic.chains.retrieval_qa.base import  RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
from utils.logger import get_logger
from utils.custom_exception import CustomException
logger=get_logger(__name__)
class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm=ChatGroq(api_key=api_key,model=model_name,temperature=0)
        self.prompt=get_anime_prompt()
        self.qa_chain=RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt":self.prompt}
        )

    def get_recommendation(self,query:str):
        try:
            result=self.qa_chain({"query":query})
            return result["result"]
        except Exception as e:
            logger.error(f"Error during get_recommendation qa_chain {str(e)}")
            raise CustomException("Error in get_recommendation ",e)

