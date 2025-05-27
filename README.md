# PDF Question Answering App

A Streamlit-based web application that allows users to upload PDF documents and ask questions about their content. The application uses advanced natural language processing and machine learning techniques to provide accurate answers based on the PDF content.

## Features

- PDF document upload and processing
- Interactive question-answering interface
- Advanced text extraction and processing
- Semantic search capabilities
- Powered by Hugging Face's FLAN-T5 model
- User-friendly Streamlit interface

## Technologies Used

- Python 3.x
- Streamlit
- LangChain
- Hugging Face Transformers
- FAISS (Facebook AI Similarity Search)
- PyPDF2
- Sentence Transformers

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd myproject
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Hugging Face API token:
   - Create an account on [Hugging Face](https://huggingface.co/)
   - Get your API token from your account settings
   - Set the environment variable:
     ```bash
     # On Windows
     set HUGGINGFACEHUB_API_TOKEN=your_token_here
     # On Unix or MacOS
     export HUGGINGFACEHUB_API_TOKEN=your_token_here
     ```

## Usage

1. Start the Streamlit application:
```bash
streamlit run steamlitapp.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload a PDF document using the file uploader

4. Once the PDF is processed, enter your question in the text input field

5. The application will process your question and display the answer based on the PDF content

## Project Structure

- `steamlitapp.py`: Main Streamlit application file
- `model.py`: Contains the PDF processing and question-answering logic
- `requirements.txt`: List of Python dependencies
- `pyproject.toml`: Project configuration file

## How It Works

1. The application uses PyPDF2 to extract text from uploaded PDF documents
2. The text is split into manageable chunks using LangChain's text splitter
3. FAISS is used to create a vector store for efficient similarity search
4. The Hugging Face FLAN-T5 model processes questions and generates answers
5. The Streamlit interface provides a user-friendly way to interact with the system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for providing the FLAN-T5 model
- Streamlit for the web application framework
- LangChain for the NLP pipeline components
