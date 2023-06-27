#### LangChain Medical Patient Summary

LangChain Medical Patient Summary is an innovative project leveraging the power of Natural Language Processing (NLP) and OpenAI's GPT-4 language model. It's designed to retrieve and summarize medical patient information from JSON formatted patient files, conforming to FHIR (Fast Healthcare Interoperability Resources) protocol.

##### How it works

1. The program reads patient data from a JSON file, then splits this data into manageable chunks.
2. It uses OpenAI embeddings to understand and analyze the text, forming the basis for question-answering.
3. Chroma, a text retriever, extracts relevant patient data from these embeddings, and limits token count to manage computational load.
4. This relevant data is then passed to a question-answering chain which uses OpenAI's GPT-4 language model, to provide interactive and informative responses to open-ended medical questions.

##### Requirements
The project requires Python 3.7 or higher and the following Python libraries:

- langchain (version that includes OpenAI GPT-4 model)
- Chroma

Please make sure you have all the required Python packages installed. You can install these packages using pip:

`pip install -r requirements.txt`

Quick Start Guide

1. Clone the repository:
`https://github.com/tom-juntunen/medagi.git`

2. Navigate to the project directory:
`cd medagi`

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
Once you have obtained your OpenAI API access token, you can proceed with the code update. 

<img width="818" alt="Screenshot 2023-06-26 at 11 41 41 PM" src="https://github.com/tom-juntunen/medagi/assets/43662466/c9850e95-b03f-41aa-a05d-5dfdc82a28e7">

