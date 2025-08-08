# 🤖 Local PDF Q&A Chatbot with RAG

A simple chatbot that answers questions based on the content of a PDF document you provide. This project uses the RAG (Retrieval-Augmented Generation) architecture and runs **100% locally** to ensure your data remains private.

This project was built as a learning exercise to understand how LangChain works with locally-run LLMs powered by Ollama.



---

## ✨ Key Features

* **Q&A with Documents**: "Talk" directly to your PDF files.
* **RAG-Powered**: Uses a Large Language Model to generate context-aware answers from your document.
* **Privacy-Focused**: All processing, from embedding to LLM inference, happens on your machine. No data is sent to external services.
* **Simple Interface**: Easy interaction through your command-line terminal.

---

## 📚 Tech Stack

* **Framework**: LangChain
* **Local LLM**: Llama 3 via Ollama
* **Embedding Model**: `all-MiniLM-L6-v2` from HuggingFace
* **Vector Store**: ChromaDB
* **PDF Reader**: PyMuPDF

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

Make sure you have **Ollama** installed and have pulled the Llama 3 model. If not, run the following command in your terminal:
```bash
ollama run llama3:8b
```

### 2. Project Setup

Clone this repository to your machine:
```bash
git clone https://github.com/aryy-hue/chatbot-rag.git
cd chatbot-rag
```

Create and activate a virtual environment:
```bash
# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

Install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1.  Place the PDF file you want to use in the project's root folder (e.g., `my_document.pdf`).
2.  Open the `app.py` file and update the `PDF_PATH` variable with your document's name: `PDF_PATH = "my_document.pdf"`.
3.  Make sure the **Ollama application is running in the background**.
4.  Run the main script:
    ```bash
    python app.py
    ```
5.  Wait for the setup process to complete. Once you see the "Setup Finish" message, you can start asking questions in the terminal!

### Example Session
```
--- Setup Finish ---
Type 'exit' or 'quit' to close

You: According to the document, what were the main achievements in 2023?

Chatbot is thinking wait for a moment...

Chatbot: Based on the document, the main achievements in 2023 were the launch of Project Phoenix, a 15% increase in user engagement, and securing Series B funding.
```

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
