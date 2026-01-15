import os
from groq import Groq
from pdf_utils import chunk_text

# Initialize Groq client (uses Streamlit Secrets or local env)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama3-70b-8192"  # supported & stable


def groq_generate(system_prompt, user_text, max_tokens=300):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        temperature=0.3,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def llm_summary(text):
    chunks = chunk_text(text, max_words=1200)
    summaries = []

    for chunk in chunks:
        summaries.append(
            groq_generate(
                "You are an academic assistant. Summarize clearly.",
                chunk,
                max_tokens=250,
            )
        )

    return "\n\n".join(summaries)


def llm_mcqs(text):
    return groq_generate(
        "Create 5 exam-oriented MCQs with answers.",
        text,
        max_tokens=400,
    )


def llm_qa(text):
    return groq_generate(
        "Generate 5 short-answer exam questions with answers.",
        text,
        max_tokens=400,
    )