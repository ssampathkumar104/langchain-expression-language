# LangChain Expression Language (LCEL) - Simple LLM Project

A practical demonstration of LangChain Expression Language (LCEL) for building composable LLM chains using the Groq API. This project showcases how to build, chain, and serve LLM components with a focus on clean, declarative syntax.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [What is LCEL?](#what-is-lcel)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Basic Setup](#basic-setup)
  - [Building Chains](#building-chains)
  - [Advanced Examples](#advanced-examples)
- [Project Structure](#project-structure)
- [API Server](#api-server)
- [Examples from Notebook](#examples-from-notebook)

---

## 🎯 Project Overview

This project demonstrates how to use **LangChain Expression Language (LCEL)** to build composable language model chains. The primary use case is **English-to-multiple-language translation** powered by the Groq API (using the fast Llama 3.1 8B model).

**Key Highlights:**
- ✨ Simple, declarative chain composition using the pipe (`|`) operator
- 🚀 Fast inference with Groq's Llama 3.1 8B model
- 📊 Jupyter notebook with step-by-step examples
- 🌐 FastAPI server for serving the translation chain as an API
- 🔧 Easy to extend with additional components

---

## 🔗 What is LCEL?

LCEL (LangChain Expression Language) is a declarative way to compose components in LangChain. Instead of writing verbose, imperative code, you can use the pipe operator (`|`) to chain components together in a readable, functional style.

**Example:**
```python
# Without LCEL (verbose)
raw_response = model.invoke(messages)
parsed_response = parser.invoke(raw_response)

# With LCEL (clean and readable)
chain = model | parser
result = chain.invoke(messages)
```

---

## ✨ Features

- **Groq API Integration**: Uses Groq's fast Llama 3.1 8B model for inference
- **LangChain Expression Language**: Demonstrates modern chain composition patterns
- **Translation Pipeline**: Pre-built chain for translating English to any language
- **FastAPI Server**: REST API endpoint for the translation service
- **Jupyter Notebook**: Complete examples and step-by-step explanations
- **Environment Configuration**: Secure API key management with `.env` files

---

## 📦 Requirements

- Python 3.8+
- Groq API key (get one at [groq.com](https://groq.com))
- Dependencies listed in `requirements.txt`

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ssampathkumar104/langchain-expression-language.git
   cd langchain-expression-language
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:
   ```bash
   touch .env
   ```

2. **Add your Groq API key:**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Verify the setup** by running the notebook or server

---

## 💡 Usage

### Basic Setup

Load environment variables and initialize the model:

```python
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
```

### Building Chains

#### Step 1: Set up components

```python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to {language}."),
    ("user", "{input}")
])

# Create an output parser
parser = StrOutputParser()
```

#### Step 2: Compose the chain with LCEL

```python
# Chain components using the pipe operator
chain = prompt | model | parser
```

#### Step 3: Invoke the chain

```python
result = chain.invoke({
    "language": "French",
    "input": "Hello, how are you?"
})
print(result)
# Output: "Bonjour, comment allez-vous ?"
```

### Advanced Examples

#### Example 1: Manual Chain Invocation

```python
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Hello, how are you?")
]

# Invoke without LCEL (traditional way)
raw_response = model.invoke(messages)
parsed_response = parser.invoke(raw_response)
print(parsed_response)
```

#### Example 2: Using LCEL with Simple Chain

```python
# Create a simple model + parser chain
chain = model | parser

result = chain.invoke(messages)
print(result)  # Output: "Bonjour, comment allez-vous ?"
```

#### Example 3: Using LCEL with Prompt Template

```python
# Complete chain: prompt → model → parser
chain = prompt | model | parser

result = chain.invoke({
    "language": "Spanish",
    "input": "Good morning!"
})
print(result)  # Output: "¡Buenos días!"
```

---

## 📁 Project Structure

```
langchain-expression-language/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (API keys)
├── SimpleLLM_LCEL.ipynb        # Jupyter notebook with examples
├── serve.py                    # FastAPI server for serving the chain
└── .gitignore                  # Git ignore file
```

**File Descriptions:**

| File | Purpose |
|------|---------|
| `SimpleLLM_LCEL.ipynb` | Interactive Jupyter notebook demonstrating LCEL concepts with step-by-step execution |
| `serve.py` | FastAPI application that exposes the translation chain as a REST API |
| `requirements.txt` | All Python package dependencies |
| `.env` | Environment variables (API keys) - create this file locally |

---

## 🌐 API Server

The project includes a FastAPI server that exposes the translation chain as a web API.

### Running the Server

```bash
python serve.py
```

The server starts at `http://localhost:8000`

### API Endpoints

#### 1. **Translation Endpoint**
- **Path:** `/translate`
- **Method:** `POST`
- **Input (JSON):**
  ```json
  {
    "language": "French",
    "input": "Hello, how are you?"
  }
  ```
- **Output (JSON):**
  ```json
  {
    "output": "Bonjour, comment allez-vous ?"
  }
  ```

#### 2. **Interactive API Documentation**
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Example API Call

Using `curl`:
```bash
curl -X POST "http://localhost:8000/translate" \
  -H "Content-Type: application/json" \
  -d '{"language": "French", "input": "Hello, how are you?"}'
```

Using Python `requests`:
```python
import requests

response = requests.post(
    "http://localhost:8000/translate",
    json={"language": "French", "input": "Hello, how are you?"}
)
print(response.json())
```

---

## 📚 Examples from Notebook

The Jupyter notebook (`SimpleLLM_LCEL.ipynb`) contains the following examples:

### 1. **Environment Setup**
```python
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
```

### 2. **Initialize ChatGroq Model**
```python
from langchain_groq import ChatGroq
model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
```

### 3. **Create Messages and Parser**
```python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Hello, how are you?")
]

parser = StrOutputParser()
```

### 4. **Direct Model Invocation**
```python
# Get raw response from model
raw_response = model.invoke(messages)
print(raw_response)  # AIMessage with French translation

# Parse the response to string
parsed_response = parser.invoke(raw_response)
print(parsed_response)  # Clean string output
```

### 5. **LCEL Chain: Model + Parser**
```python
# Compose using LCEL (the pipe operator)
chain = model | parser
result = chain.invoke(messages)
print(result)  # Output: "Bonjour, comment allez-vous ?"
```

### 6. **Create Prompt Template**
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to {language}."),
    ("user", "{input}")
])
```

### 7. **Complete LCEL Chain: Prompt + Model + Parser**
```python
# Full chain with variables
chain = prompt | model | parser

result = chain.invoke({
    "language": "French",
    "input": "Hello, how are you?"
})
print(result)
```

---

## 🎓 Learning Outcomes

By exploring this project, you'll learn:

1. ✅ How to use LangChain Expression Language (LCEL) for declarative chain composition
2. ✅ How to integrate with Groq API for fast LLM inference
3. ✅ How to create reusable prompt templates
4. ✅ How to build output parsers for structured responses
5. ✅ How to serve LLM chains as REST APIs using FastAPI
6. ✅ Best practices for managing API keys and environment variables
7. ✅ How to test and invoke LLM chains programmatically

---

## 🔧 Troubleshooting

### Issue: `GROQ_API_KEY not found`
**Solution:** Ensure your `.env` file exists and contains the correct API key
```env
GROQ_API_KEY=your_actual_api_key_here
```

### Issue: `ModuleNotFoundError` for dependencies
**Solution:** Make sure all dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Server won't start
**Solution:** Check if port 8000 is already in use
```bash
# Use a different port
python serve.py --port 8001
# Or kill the process using port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

---

## 📖 References

- [LangChain Documentation](https://python.langchain.com/)
- [LCEL Documentation](https://python.langchain.com/docs/expression_language/)
- [Groq API](https://groq.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangServe](https://github.com/langchain-ai/langserve)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

---

**Happy chaining! 🚀**
