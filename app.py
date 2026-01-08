import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI PDF Study Assistant", layout="centered")

st.title("📄 AI PDF Study Assistant")
st.write("Upload a PDF and generate summaries, MCQs, and exam questions.")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    # Extract text
    pdf_text = extract_text_from_pdf(uploaded_file)

    # DEBUG: show text length
    st.info(f"Extracted {len(pdf_text)} characters from PDF")

    # Show button ONLY after extraction
    if st.button("✨ Generate Output"):
        if len(pdf_text.strip()) == 0:
            st.error("No text found in PDF (scanned PDF maybe).")
        else:
            st.subheader("📘 Extracted Text Preview")
            st.text_area("Preview", pdf_text[:3000], height=300)
