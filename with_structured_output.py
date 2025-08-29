from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

llm= HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.1", task="text-generation", max_new_tokens=100)

model= ChatHuggingFace(llm=llm)

# Create Schema to show that how the output may look like

class Review(TypedDict):
    summary : str
    sentiment: str

structured_model= model.with_structured_output(Review)

result= structured_model.invoke(""" The hardware is great but software feels bloated. There are too many pre-installed applications that I can't remove. Also, UI looks outdated compare to other brands. Hoping software update to fix it""", stop=["<|tool calls begin|>"])

print(result)
print(result["summary"])
print(result["sentiment"])