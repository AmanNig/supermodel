import streamlit as st
import PyPDF2


def myapp():

    # Streamlit app layout
    st.set_page_config(page_title="PDF QA App", layout="centered")
    st.title("📄 PDF Question Answering App")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file:
        # Extract PDF content
        pdf_text = None
        with st.spinner("Reading Your PDF..."):
            from model import extract_pdf
            pdf_text = extract_pdf(uploaded_file)

        st.success("Read Whole Pdf successfully!")


        # User question input
        user_question = st.text_input("Ask a question based on the PDF content")

        if user_question:
            st.info(f"Your question: {user_question}")
            answer=None
            with st.spinner("Generating Answer..."):
                from model import myModel
                answer = myModel(pdf_text,user_question)

            st.success("Answer Generated Successfully!")
            
            # TODO: Add your model logic here
            # Example (placeholder):
            # answer = my_model_answer(pdf_text, user_question)
            # answer = "This is a placeholder answer. Replace this with your model output."

            st.markdown("### 📌 Answer:")
            st.write(answer)


if __name__=="__main__":
    myapp()
    