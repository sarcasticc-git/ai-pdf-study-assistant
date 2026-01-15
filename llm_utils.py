import ollama
from pdf_utils import chunk_text


def summarize_chunk(chunk):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "system",
                "content": "Summarize the following academic content clearly."
            },
            {
                "role": "user",
                "content": chunk
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 150
        }
    )
    return response["message"]["content"]


def generate_mcqs(chunk):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "system",
                "content": "Generate 5 exam-oriented multiple choice questions with 4 options and correct answers."
            },
            {
                "role": "user",
                "content": chunk
            }
        ],
        options={
            "temperature": 0.3,
            "num_predict": 250
        }
    )
    return response["message"]["content"]


def generate_qa(chunk):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "system",
                "content": "Generate 5 important exam questions with short answers."
            },
            {
                "role": "user",
                "content": chunk
            }
        ],
        options={
            "temperature": 0.3,
            "num_predict": 250
        }
    )
    return response["message"]["content"]


def llm_summary(text):
    chunks = chunk_text(text, chunk_size=300)
    summaries = []

    for i, chunk in enumerate(chunks, start=1):
        summaries.append(f"### Part {i}\n{summarize_chunk(chunk)}")

    return "\n\n".join(summaries)


def llm_mcqs(text):
    chunks = chunk_text(text, chunk_size=500)
    return generate_mcqs(chunks[0])   # first chunk is enough for MCQs


def llm_qa(text):
    chunks = chunk_text(text, chunk_size=500)
    return generate_qa(chunks[0])
