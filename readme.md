# 📌 Customer Support AI Agent

## 📖 Project Overview
This project is a **Customer Support AI Agent** designed for an e-commerce platform. The AI agent uses **Retrieval-Augmented Generation (RAG)** to answer customer queries based on a predefined knowledge base. It retrieves relevant product information and company policies using **ChromaDB** and generates responses with **Google Gemini AI**.

## 🚀 Features
- **Retrieval-Augmented Generation (RAG):** Enhances responses with relevant knowledge.
- **ChromaDB Integration:** Stores and retrieves product details efficiently.
- **Google Gemini AI:** Generates intelligent responses based on retrieved data.
- **Automatic Knowledge Base Update:** Detects changes in the knowledge base and updates ChromaDB accordingly.
- **Logging:** Tracks queries and responses for debugging and improvements.

## 🛠️ Installation
### Prerequisites
Ensure you have the following installed:
- Python latest version
- Required Python libraries such as chromadb, google.generativeai, etc.

### Setup Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/oranger123/ASTUDIO-Task.git
   cd ASTUDIO-Task
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your **Google API Key** in an environment variable:
   - Obtain a free-tier API key from Google AI.
   - Replace the placeholder in the script with your API key:
     ```python
     os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
     ```
5. Start the query engine:
   ```sh
   python query_data.py
   ```
## Updating the Knowledge Base
- If you add new products or policy details to `ecommerce_knowledge_base.txt`, the query_data.py file automatically retrieves the new informations and store it in chromadb.
-This ensures the ChromaDB vector store is updated with the latest information.

## 📌 Usage
- When prompted, enter a customer query (e.g., *"What is your return policy?"*).
- The AI will retrieve relevant data and generate a response.
- Type **exit** to quit the program.

## 🔍 Troubleshooting
- **No relevant information found?**
  - Ensure `ecommerce_knowledge_base.txt` contains the required details.
- **Google Gemini AI not responding?**
  - Verify your API key is correct and has sufficient quota.
  - Try changing the model to `gemini-2.0-flash` for free-tier access.
- **Script errors?**
  - Check `query_logs.txt` for details on failures.

## 📌 Developed By: Sriuma S  
📧 Contact: sriuma2001s@gmail.com