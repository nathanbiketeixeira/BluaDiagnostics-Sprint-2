from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

vectordb = Chroma(
    persist_directory="vector_db",
    embedding_function=OpenAIEmbeddings()
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})


def buscar_contexto(query):
    docs = retriever.get_relevant_documents(query)
    return [doc.page_content for doc in docs]
