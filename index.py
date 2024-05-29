from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

pdf_file_path = "C:/Users/AnjanaMurali/Desktop/qdrant/database-concepts.pdf"

loader = PyPDFLoader(pdf_file_path)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)
text  = text_splitter.split_documents(documents)

model_name ="BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

embeddings = HuggingFaceBgeEmbeddings(
    model_name = model_name,
    model_kwargs =model_kwargs,
    encode_kwargs = encode_kwargs
)

print("Embeddings Model Loaded...........")

url="http://localhost:6333"
collection_name="gpt_db"


qdrant = Qdrant.from_documents(
    text,
    embeddings,
    url = url,
    prefer_grpc = False,
    collection_name = collection_name
    )

print("Qdrant Index Created ..............")
