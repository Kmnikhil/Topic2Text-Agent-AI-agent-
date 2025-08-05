# from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",task="text-generation", temperature=0.7,
    huggingfacehub_api_token="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"
)
# lm = HuggingFaceEndpoint(repo_id=repo_id, task="text-generation", temperature=0.7, huggingfacehub_api_token=sec_key)
response = llm.invoke("What is the capital of France?")
print(response)