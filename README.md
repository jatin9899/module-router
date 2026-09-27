# 🤖 Module Router

A simple **LLM Model Router** built with Python and LangChain that automatically analyzes a user's query and selects an appropriate AI model based on its complexity.

## 🚀 How It Works

The project follows a 4-step pipeline:

1. **Query Optimization**  
   The user's query is rewritten into a clearer and more structured prompt using `gpt-4o-mini`.

2. **Query Classification**  
   The optimized query is classified as either:
   - `simple`
   - `complex`

3. **Model Routing**  
   Based on the classification:
   - Simple queries → `gpt-4o-mini`
   - Complex queries → `gpt-4o`

4. **Final Response**  
   The selected model generates the final answer.

### 🔄 Flow

```text
User Query
    ↓
Query Optimizer
    ↓
Complexity Classifier
    ↓
Simple ──────────→ gpt-4o-mini
    │
Complex ─────────→ gpt-4o
    ↓
Final Answer
```

## 🛠️ Technologies Used

- Python
- LangChain
- OpenAI API
- LangChain OpenAI
- python-dotenv

## 📁 Project Structure

```text
module-router/
│
├── module_router.py
├── .gitignore
└── README.md
```

> The `.env` file is used locally for the OpenAI API key and is excluded from Git using `.gitignore`.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/jatin9899/module-router.git
cd module-router
```

### 2. Install dependencies

```bash
pip install langchain-openai python-dotenv
```

### 3. Create a `.env` file

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Never commit or share your API key.**

### 4. Run the project

```bash
python module_router.py
```

## 💡 Example

Input:

```text
Plan 15 days holiday in Europe with a budget of $3000.
```

The router:

```text
User Query
     ↓
Optimize Query
     ↓
Classify Complexity
     ↓
Complex
     ↓
gpt-4o
     ↓
Final Answer
```

## 🎯 Purpose

This project demonstrates a basic **AI model routing architecture**, where different models can be selected dynamically depending on the complexity of a user's request.



## 👨‍💻 Author

**Jatin Saini**

GitHub: [@jatin9899](https://github.com/jatin9899)
