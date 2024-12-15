import os
import openai
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

documents = SimpleDirectoryReader('articles').load_data()

index = VectorStoreIndex.from_documents(documents)

# llama index 0.6 replaces index.save_to_disk() with index.storage_context.persist()
# json files will be stored in a storage/ directory instead of index_new.json
# index.save_to_disk('index_news.json')

index.storage_context.persist()