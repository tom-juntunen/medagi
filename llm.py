from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
import os

from pusher import Pusher
import time
import os

# Read JSON file
with open('patient.json', 'r') as file:
    text = file.read()

with open("patient.json") as f:
    patient_data = f.read()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(patient_data)

embeddings = OpenAIEmbeddings()

query1 = 'Return me one single patient record.'
docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]).as_retriever()
docs = docsearch.get_relevant_documents(query1)
docs[0].page_content = docs[0].page_content[:2500]

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query2 = f"""You are medical expert who also knows JSON and FHIR protocol. 
Summarise the info about the patient based on the given FHIR JSON data."""

msg = chain.run(input_documents=docs, question=query2)

# instantiate the Pusher class with your appId, key, secret and cluster
PUSHER_APP_ID = os.environ["PUSHER_APP_ID"]
PUSHER_API_KEY = os.environ["PUSHER_API_KEY"]
CLUSTER = 'us3'
PUSHER_SECRET = os.environ["PUSHER_SECRET"]

pusher_client = Pusher(
  app_id=PUSHER_APP_ID,
  key=PUSHER_API_KEY,
  secret=PUSHER_SECRET,
  cluster=CLUSTER,
  ssl=True
)

# trigger an event to a channel. channel-name and event-name can be custom
pusher_client.trigger('General', 'new-message', 
                      {'id': 'message-123', 'user': 'medAGI', 'message': msg}
)

def callback(data):
    print('received %s' % data)

import pusherclient
import time

# replace with your pusher key
pusherkey = PUSHER_API_KEY
pusher_c = pusherclient.Pusher(key=pusherkey, secret=PUSHER_SECRET)

# define callback function to process event
def print_callback(data):
    print(data)

def connect_handler(data):
    try:
        channel = pusher_c.subscribe('General')
        channel.bind('new-message', print_callback)
    except RuntimeError as e:
        print(f"RuntimeError occurred: {e}")
        # handle the error here or just pass

pusher_c.connection.bind('pusher:connection_established', connect_handler)
pusher_c.connect()

while True:
    # Keep the main thread alive and the connection with Pusher persistent
    time.sleep(1)
