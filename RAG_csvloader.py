from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv")

documents = loader.load()

print(type(documents))

print(len(documents))

print(documents[1])