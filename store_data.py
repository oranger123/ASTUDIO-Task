import chromadb
import uuid

# Initialize Chroma DB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="ecommerce_knowledge")

# Read knowledge base file
with open("ecommerce_knowledge_base.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Split into smaller sections (modify based on your file format)
sections = content.split("\n\n")

# Store each section separately
for idx, section in enumerate(sections):
    if section.strip():  # Ignore empty sections
        section_id = str(uuid.uuid4())  # Generate unique ID
        collection.add(
            documents=[section],
            ids=[section_id],
            metadatas=[{"index": idx}]  # Optional metadata
        )

print("Knowledge base stored successfully in Chroma DB!")
