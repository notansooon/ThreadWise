from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import os

from langcahin.prompts import PromptTemplate, ChatPromptTemplate

# Initialize OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


PromptTemplate = PromptTemplate(
    input_variables=["context", "question"],
    template="You are a helpful assistant. Use the following context to answer the question.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
)

ChatPrompt = ChatPromptTemplate.from_te

def processData(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )
    texts = text_splitter.split_text(data)
    return texts

def embedData(data, save_path="vectorstore"):
    embedding = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=OPENAI_API_KEY
    )
    texts = processData(data)
    
    vectorstore = FAISS.from_texts(
        texts=texts,
        embedding=embedding
    )
    
    vectorstore.save_local(save_path)
    return vectorstore

def load_vectorstore(load_path="vectorstore"):
    # Load the vector store from disk
    return FAISS.load_local(load_path, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))

def query_vectorstore(query, vectorstore, k=5):
    # Perform a similarity search
    return vectorstore.similarity_search(query, k=k)

