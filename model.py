
def extract_pdf(uploaded_file):
    from PyPDF2 import PdfReader

    pdfreader = PdfReader(uploaded_file)

    from typing_extensions import Concatenate
    # read text from pdf
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content


    from langchain.text_splitter import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],  # Tries larger to smaller separators
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
    )

    texts = text_splitter.split_text(raw_text)
    return texts


def myModel(texts,query:str)->str:
    
    from typing_extensions import Concatenate
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import FAISS





    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain_community.llms import HuggingFaceHub
    # For embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # For LLM using HuggingFace Hub (online)
    from langchain_community.llms import HuggingFaceHub


    llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature":0.5, "max_length":512})

    document_search = FAISS.from_texts(texts, embeddings)

    from langchain.chains.question_answering import load_qa_chain
    from langchain_community.llms import HuggingFaceHub
    chain = load_qa_chain(llm, chain_type="stuff")

    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    from langchain_community.llms import HuggingFaceHub
    from huggingface_hub import InferenceClient # Import InferenceClient

    import os
    #os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_hf_token_here"  # Replace with real token (You already set this earlier)

    # Use a FLAN model that supports inference (seq2seq task)
    # Instantiate InferenceClient explicitly for the task
    client = InferenceClient(model="google/flan-t5-base") # Specify model here

    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base", # repo_id is still needed for HuggingFaceHub structure
        task="text2text-generation",  # Required for FLAN-T5
        client=client, # Pass the instantiated client
        model_kwargs={"temperature": 0.5, "max_length": 512}
    )

    # Prompt template
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    )

    # Build the chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Query
    # query = "what is Shape Memory Alloys"

    
    docs = document_search.similarity_search(query)

    # Merge documents into context
    context = "\n\n".join([doc.page_content for doc in docs])
        
        # ✅ Use `.invoke()` instead of `.run()` (new standard)
    #response = llm_chain.invoke({"context": context, "question": query})

    print(context)  # Output final answer
    return context