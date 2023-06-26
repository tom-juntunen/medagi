# medagi
LangChain Medical Patient Summary

This project reads a patient's FHIR-formatted JSON record, extracts relevant information, and uses OpenAI's language model to create a summary of the patient's information. The summary is then sent as a message over a Pusher channel.

How it works

The project first reads a FHIR-formatted JSON file that contains a patient's medical record.
The text from this file is split into chunks of 1000 characters each.
The Chroma class, powered by OpenAI embeddings, is used to convert these text chunks into vectors.
A question-answering chain is loaded using the OpenAI language model.
A query is then made to this chain to generate a summary of the patient's information. The output of this query is a summary text.
This summary is then sent as a message over a Pusher channel, 'General', with the event name 'new-message'.
The message is then received on the same channel using the pusherclient library.
Requirements

Python 3.x
pusher
pusherclient
langchain
openai
Please make sure you have all the required Python packages installed. You can install these packages using pip:
