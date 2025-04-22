from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import os

from langchain.prompts import PromptTemplate, ChatPromptTemplate


from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA

# Initialize OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

PromptTemplate = PromptTemplate.from_template(
    
    "You are an expert assistant that rephrases questions for better memory retrieval.\n"
    "Generate multiple variations of this question to help find relevant information:\n\n"
    "{question}"
)

ChatPrompt = ChatPromptTemplate.from_messages(
    {
        ("system", "You are a helpful assistant for summarizing memory chunks."),
        ("human", "Here are the chunks: {context}\n\nQuestion: {question}")
    }
    
)


def get_retriever():
    try:
        
        vectorstore = load_vectorstore()
        retriever = MultiQueryRetriever.from_llm(
            llm = llm,
            retriever = vectorstore.as_retriever(),
            PromptTemplate = PromptTemplate,
        
        )
        return retriever
    except Exception as e:
        print(f"Error in get_retriever: {e}")
        return None
    


def get_response(query):
    retreiver = get_retriever()
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retreiver,  
        chain_type="stuff",      
        return_source_documents=True
    )
    
    response = chain.run(query)
    
    return response



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
    
    # save the vector store to AWS later on
    vectorstore.save_local(save_path)
    return vectorstore

def load_vectorstore(load_path="vectorstore"):
    # Load the vector store from disk
    return FAISS.load_local(load_path, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))

def query_vectorstore(query, vectorstore, k=5):
    # Perform a similarity search
    return vectorstore.similarity_search(query, k=k)

