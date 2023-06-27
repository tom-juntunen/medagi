LangChain Medical Patient Summary

This project reads a patient's FHIR-formatted JSON record, extracts relevant information, and uses OpenAI's language model to create a summary of the patient's information. The summary is then sent as a message over a Pusher channel.

How it works

The project first reads a FHIR-formatted JSON file that contains a patient's medical record. The text from this file is split into chunks of 1000 characters each. The Chroma class, powered by OpenAI embeddings, is used to convert these text chunks into vectors. A question-answering chain is loaded using the OpenAI language model. A query is then made to this chain to generate a summary of the patient's information. The output of this query is a summary text. This summary is then sent as a message over a Pusher channel named 'General' with the event name 'new-message'. The message is received on the same channel using the pusherclient library.

Requirements

- Python 3.x
- pusher
- pusherclient
- langchain
- openai

Please make sure you have all the required Python packages installed. You can install these packages using pip:

pip install pusher pusherclient langchain openai

Quick Start Guide

1. Clone the repository:
`https://github.com/tom-juntunen/medagi.git`

2. Navigate to the project directory:
`cd langchain-medical-patient-summary`

3. Install the required Python packages:
`pip install -r requirements.txt`

4. Prepare the patient data:
- Ensure you have a FHIR-formatted JSON file containing the patient's medical record. Let's assume the file is named `patient.json`.
- Place the `patient.json` file in the project directory.

5. Run the application:
`python llm.py`

6. Follow the prompts in the command line interface:
- When prompted, describe your difficulties and the challenges you are facing.
- If prompted again, provide any other difficulties.
- The application will generate a summary of the patient's information based on your input.

7. Observe the output:
- The generated summary will be displayed in the command line interface.
- The summary will also be sent as a message over the Pusher channel named 'General' with the event name 'new-message'.

Congratulations! You have successfully run the LangChain Medical Patient Summary application. Feel free to explore the code and make any necessary changes to suit your requirements.

Before proceeding with the code update, please note that you will need an OpenAI account and an OpenAI API access token to use the OpenAI models. Here are the steps to acquire the necessary credentials:

Create an OpenAI account: If you don't have an account, visit the OpenAI website (https://www.openai.com) and sign up for an account.
Generate an OpenAI API access token:
Log in to your OpenAI account.
Navigate to the API section of your account dashboard.
Follow the instructions provided by OpenAI to generate an API access token.
Take note of the generated API access token, as you will need it to authenticate your API requests.
Once you have obtained your OpenAI API access token, you can proceed with the code update. Replace the following line:
