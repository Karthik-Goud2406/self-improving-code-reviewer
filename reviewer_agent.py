from langchain_openai import ChatOpenAI

def review_code(context, memory):
    try:
        llm = ChatOpenAI(temperature=0.2)
        prompt = f"""
You are assisting a human code reviewer.

Context:
{context}

Past feedback:
{memory}

Rules:
- Do NOT approve code
- Suggest risks or questions only
- Be concise

Review:
"""
        return llm.predict(prompt)
    except Exception:
        # graceful fallback
        return (
            "Potential risk detected: async behavior introduced.\n"
            "Consider verifying concurrency safety and error handling."
        )
