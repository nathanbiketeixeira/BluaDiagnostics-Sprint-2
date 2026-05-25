from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

paths = [
    "data/knowledge_base/protocolo_hipertensao.txt",
    "data/knowledge_base/protocolo_respiratorio.txt",
    "data/knowledge_base/politica_telemedicina.txt",
    "data/knowledge_base/bula_losartana.txt",
    "data/knowledge_base/cartilha_prevencao.txt"
]

all_docs = []

for path in paths:
    loader = TextLoader(path)
    docs = loader.load()
    all_docs.extend(docs)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(all_docs)

vectordb = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(),
    persist_directory="vector_db"
)

vectordb.persist()
