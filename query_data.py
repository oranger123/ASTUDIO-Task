import chromadb
import google.generativeai as genai
import os
import subprocess  # To run store_data.py automatically
import logging

# Set up logging
logging.basicConfig(
    filename="query_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Set up Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDw_qyXDwUimZpqzO6NwSbxF9nenNs6Q3I"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# File tracking (to detect changes)
DATA_FILE = "ecommerce_knowledge_base.txt"
LAST_MODIFIED_FILE = "last_modified.txt"


def get_last_modified_time():
    """Get the last modified time of the knowledge base file."""
    return os.path.getmtime(DATA_FILE) if os.path.exists(DATA_FILE) else 0


def store_last_modified_time(timestamp):
    """Store the last modified time to track updates."""
    with open(LAST_MODIFIED_FILE, "w") as f:
        f.write(str(timestamp))


def get_stored_modified_time():
    """Retrieve the last stored modified time."""
    if os.path.exists(LAST_MODIFIED_FILE):
        with open(LAST_MODIFIED_FILE, "r") as f:
            return float(f.read().strip())
    return 0


def check_and_update_knowledge_base():
    """Check if the knowledge base file has changed and update ChromaDB if needed."""
    current_modified_time = get_last_modified_time()
    stored_modified_time = get_stored_modified_time()

    if current_modified_time > stored_modified_time:
        print("🔄 Detected changes in knowledge base. Updating ChromaDB...")
        try:
            subprocess.run(["python", "store_data.py"], check=True)  # ✅ Check for errors
            store_last_modified_time(current_modified_time)
            print("✅ Knowledge base updated successfully!")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to update ChromaDB: {e}")
            print("❌ Error updating ChromaDB. Check logs for details.")


# Check and update knowledge base before querying
check_and_update_knowledge_base()

# Initialize Chroma DB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="ecommerce_knowledge")


# Function to retrieve data from ChromaDB
def retrieve_data(query, n_results=2):
    try:
        results = collection.query(query_texts=[query], n_results=n_results)
        documents = results.get("documents", [])  # ✅ Fix: Avoids KeyError
        return " ".join(documents[0]) if documents else "No relevant information found."
    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
        return "Error retrieving information."


# Function to generate AI response
def generate_response(query):
    retrieved_text = retrieve_data(query)
    model = genai.GenerativeModel("gemini-2.0-flash")  # Use free-tier model
    try:
        response = model.generate_content(f"Based on this information: {retrieved_text}, answer this question: {query}")
        ai_response = response.text.strip() if hasattr(response, "text") and response.text else "AI could not generate a response."
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        ai_response = "An error occurred while generating the response."

    # Log the query and response
    logging.info(f"Query: {query} | Response: {ai_response}")

    return ai_response


# Main function to interact
if __name__ == "__main__":
    while True:
        user_query = input("\nAsk a question (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        response = generate_response(user_query)
        print("\n🔹 AI Response:", response)
