from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    "docs",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

documents = loader.lazy_load()
for doc in documents:
    print(doc.metadata)