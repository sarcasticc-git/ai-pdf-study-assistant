import streamlit as st
from pdf_utils import extract_text_from_pdf
from llm_utils import llm_summary, llm_mcqs, llm_qa

st.set_page_config(page_title="AI PDF Study Assistant", layout="centered")

st.title("📄 AI PDF Study Assistant")
st.write("Upload a PDF and generate summaries, MCQs, and exam questions.")

# User control
full_summary = st.checkbox(
    "Generate full summary (may take longer on mobile devices)",
    value=False
)

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    if not pdf_text.strip():
        st.error("Could not extract text from this PDF.")
        st.stop()

    st.subheader("Choose an action")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📌 Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = llm_summary(
                    pdf_text,
                    full=full_summary
                )
            st.text_area("Summary", summary, height=350)

    with col2:
        if st.button("📝 Generate MCQs"):
            with st.spinner("Generating MCQs..."):
                mcqs = llm_mcqs(pdf_text)
            st.text_area("MCQs", mcqs, height=350)

    with col3:
        if st.button("❓ Generate Q&A"):
            with st.spinner("Generating Q&A..."):
                qa = llm_qa(pdf_text)
            st.text_area("Q&A", qa, height=350)