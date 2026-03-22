from langchain_community.document_loaders import TextLoader

loader = TextLoader("DAX_Formulaes.txt", encoding="utf8")
documents = loader.load()

# print(documents)

print(type(documents))

print(len(documents))

print(documents[0])

print(type(documents[0]))

print(documents[0].page_content)
print(documents[0].metadata)