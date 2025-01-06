import os
from dotenv import load_dotenv

from services.llm_service import get_llm

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

os.getenv("LANGCHAIN_API_KEY")

MODEL_NAME = "gpt-4o"
llm = get_llm(MODEL_NAME)