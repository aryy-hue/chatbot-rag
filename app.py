import os 
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

PDF_PATH = "oppenheimer.pdf"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OLLAMA_MODEL = "llama3:8b"

def main():
    print("--- Starting Proses ---")
    print(f"Reading document: {PDF_PATH}...")
    loader = PyMuPDFLoader(PDF_PATH)
    documents = loader.load()

    if not documents:
        print("Cannot read the document or document is empty...")
        return
    print("Breaking a document into smaller parts(Chunks)....")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    if not texts:
        print("Failed to split document")
        return
    
    print(f"Creating embeddings using models: {EMBEDDING_MODEL}...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, 
                                       model_kwargs={'device':'cpu'}) # Delete this if your cuda version is 7.0++

    print("Saving chunks to ChromaDB (vector store)...")
    vector_store = Chroma.from_documents(documents=texts, embedding=embeddings)

    print(f"Initialize LLM from Ollama with model: {OLLAMA_MODEL}")
    llm = Ollama(model=OLLAMA_MODEL)

    retriever = vector_store.as_retriever()

    print(f"Creating chain Q&A (RetrievalQA chain)...")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    print("--- Setup Finish ---")
    print("Type 'exit' or 'quit' to close")

    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break 
        print("Chatbot is thinking wait for a moment...")
        try:
            result= qa_chain.invoke(query)
            print("\nChatbot: ", result['result'])
        except Exception as e:
            print(f"Error : {e}")

if __name__ == "__main__":
    main()

