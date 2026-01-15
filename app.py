import streamlit as st
from pdf_utils import extract_text_from_pdf
from llm_utils import llm_summary, llm_mcqs, llm_qa

st.set_page_config(page_title="AI PDF Study Assistant", layout="centered")

st.title("📄 AI PDF Study Assistant")
st.write("Upload a PDF and generate summaries, MCQs, and exam questions.")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    pdf_text = extract_text_from_pdf(uploaded_file)

    if pdf_text.strip():
        st.subheader("Choose an action")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📌 Generate Summary"):
                with st.spinner("Generating summary..."):
                    st.subheader("Summary")
                    st.write(llm_summary(pdf_text))

        with col2:
            if st.button("📝 Generate MCQs"):
                with st.spinner("Generating MCQs..."):
                    st.subheader("MCQs")
                    st.write(llm_mcqs(pdf_text))

        with col3:
            if st.button("❓ Generate Q&A"):
                with st.spinner("Generating Q&A..."):
                    st.subheader("Q&A")
                    st.write(llm_qa(pdf_text))
    else:
        st.warning("Could not extract text from PDF.")
