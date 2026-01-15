import os
from groq import Groq
from pdf_utils import chunk_text

MODEL = "llama-3.1-8b-instant"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SAFE_CHUNKS = 5       # mobile-safe
FULL_CHUNKS = 20      # desktop full summary


def groq_generate(system_prompt, user_text, max_tokens=180):
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


def llm_summary(text, full=False):
    chunks = chunk_text(text)

    if full:
        chunks = chunks[:FULL_CHUNKS]
    else:
        chunks = chunks[:SAFE_CHUNKS]

    summaries = []

    for chunk in chunks:
        try:
            summaries.append(
                groq_generate(
                    "You are an academic assistant. Summarize clearly.",
                    chunk
                )
            )
        except Exception:
            summaries.append("⚠️ Error summarizing part of the document.")

    return "\n\n".join(summaries)


def llm_mcqs(text):
    chunks = chunk_text(text)[:3]
    return groq_generate(
        "Create 5 exam-oriented MCQs with options and correct answers.",
        "\n".join(chunks),
        max_tokens=300,
    )


def llm_qa(text):
    chunks = chunk_text(text)[:3]
    return groq_generate(
        "Generate 5 short-answer exam questions with answers.",
        "\n".join(chunks),
        max_tokens=300,
    )