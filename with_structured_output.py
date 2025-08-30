from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

llm= HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.1", task="text-generation", max_new_tokens=100)

model= ChatHuggingFace(llm=llm)

# Create Schema to show that how the output may look like

class Review(TypedDict):
    key_themes:Annotated[list[str], "write down all the key themes discussed in the review in the list"]
    summary : Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiments of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside the list"]

structured_model= model.with_structured_output(Review)

result= structured_model.invoke(""" The Samsung Galaxy M35 5G is a well-balanced mid-range smartphone with a sleek design, smooth AMOLED 120Hz display, and reliable 5G performance. It packs a capable 50MP camera setup and a long-lasting 6000mAh battery that ensures excellent backup. The One UI software experience is clean and user-friendly. However, it lacks fast charging compared to rivals and its plastic build may feel less premium. Overall, it’s a strong option for those who prioritize display quality, battery life, and Samsung’s ecosystem over raw power.
                                Pros: Smooth 120Hz AMOLED display, long-lasting 6000mAh battery, good 50MP camera performance, and clean Samsung One UI experience.
                                Cons: Slow charging speed, average plastic build, and not the most powerful processor in its price range.""", stop=["<|tool calls begin|>"])

print(result)
print(result["summary"])
print(result["sentiment"])