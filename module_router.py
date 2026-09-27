
print("MODULE ROUTER STARTED")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

# Models
mini_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
complex_model = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Optimizer Chain
optimizer = (
    ChatPromptTemplate.from_messages([
        ("system", "Rewrite the user's query to be clear and structured. Do not answer."),
        ("human", "{query}")
    ]) | mini_model | StrOutputParser()
)

# Classifier Chain
classifier = (
    ChatPromptTemplate.from_messages([
        ("system", """Classify as simple or complex.
        Return JSON:{{"complexity": "simple"}} or {{"complexity": "complex"}}"""),
        ("human", "{optimized_query}")
    ]) | mini_model | JsonOutputParser()
)

def route(user_query):
    # Step 1: Optimize
    optimized = optimizer.invoke({"query": user_query})

    # Step 2: Classify
    classification = classifier.invoke({"optimized_query": optimized})
    complexity = classification["complexity"]

    # Step 3: Route
    model = complex_model if complexity == "complex" else mini_model

    # Step 4: Generate final answer
    final_answer = model.invoke(optimized).content

    # Return all info
    return {
        "original_query": user_query,
        "optimized_prompt": optimized,
        "complexity": complexity,
        "selected_model": "gpt-4o" if complexity == "complex" else "gpt-4o-mini",
        "final_answer": final_answer
    }


# Example
result = route("Plan 15 days holiday in Europe with a budget of $3000.")

print("\n🔹 Original Query:\n", result["original_query"])
print("\n🔹 Optimized Prompt:\n", result["optimized_prompt"])
print("\n🔹 Complexity:\n", result["complexity"])
print("\n🔹 Selected Model:\n", result["selected_model"])
print("\n🔹 Final Answer:\n", result["final_answer"])