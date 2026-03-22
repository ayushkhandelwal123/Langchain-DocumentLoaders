from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("DL_Notes.pdf")
documents = loader.load()

for doc in documents:
    print(doc.metadata)