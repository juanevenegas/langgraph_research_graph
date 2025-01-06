from langchain_openai import ChatOpenAI

def get_llm(model: str, temperature: float = 0):
    return ChatOpenAI(model=model, temperature=temperature, max_tokens=15000)
