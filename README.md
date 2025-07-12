
# 💬 RAG Chatbot with Context Memory  
A conversational AI chatbot using Retrieval-Augmented Generation (RAG) with memory. Built with LangChain, OpenAI, FAISS, and Streamlit.  
  
## 🧠 Features  
- Context-aware Q&A from custom documents  
- Uses FAISS vector index for fast semantic search  
- Dual interface: Streamlit (frontend) + FastAPI (backend)  
- LangChain memory for conversational flow  
  
## 📁 Project Structure  
```
rag-chatbot/  
├── data/docs/              # Your document PDFs or text files  
├── src/  
│   ├── chatbot_app.py      # Streamlit UI  
│   └── api.py              # FastAPI backend  
├── vector_store/           # FAISS index stored here  
├── requirements.txt  
├── LICENSE  
├── README.md  
```  
  
## 🚀 How to Run  
  
### 1. Install dependencies  
```bash  
pip install -r requirements.txt  
```  
  
### 2. Start the chatbot (Streamlit UI)  
```bash  
streamlit run src/chatbot_app.py  
```  
  
### 3. Optional: Start backend API  
```bash  
uvicorn src.api:app --reload  
```  
  
## 📚 Data  
- Store your PDFs or `.txt` files in `data/docs/`  
- FAISS index will be created in `vector_store/` after first run  
  
## 🛠️ Tech Stack  
- Python, LangChain, OpenAI API  
- FAISS (vector DB), Streamlit  
- FastAPI (backend), PyPDF, Tiktoken  
