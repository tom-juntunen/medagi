import time

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain


def read_patient_data(file_path):
    with open(file_path) as f:
        return f.read()


def split_text_into_chunks(text, chunk_size, chunk_overlap):
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)


def load_embeddings():
    return OpenAIEmbeddings()


def get_relevant_documents(texts, embeddings):
    query = 'Return me one single patient record.'
    docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]).as_retriever()
    docs = docsearch.get_relevant_documents(query)
    docs[0].page_content = docs[0].page_content[:2500]  # limit token count
    return docs


def load_question_answering_chain():
    return load_qa_chain(OpenAI(model='text-davinci-003'), chain_type="stuff")


def run_interview(docs, chain, query, interview):
    msg = chain.run(input_documents=docs, question=query + ' ' + interview)
    return msg


if __name__ == "__main__":
    file_path = "patient.json"
    patient_data = read_patient_data(file_path)

    chunk_size = 1000
    chunk_overlap = 0
    texts = split_text_into_chunks(patient_data, chunk_size, chunk_overlap)

    embeddings = load_embeddings()

    docs = get_relevant_documents(texts, embeddings)

    chain = load_question_answering_chain()

    query = """You are a medical expert who also knows JSON and FHIR protocol. 
    Read the info about the patient based on the given FHIR JSON data and this additional info. 
    Ask open-ended questions about the location of the problem, how long it has occurred, 
    and how severe the issue is as if you are speaking with the patient directly."""

    i = 0
    msg = ''
    while True:
        q = "Describe your difficulties and the challenges you are facing:\n"
        q2 = f"{msg}:\n"
        interview = input(q if i == 0 else q2)
        msg = run_interview(docs, chain, query, interview)
        i += 1
        time.sleep(3)
