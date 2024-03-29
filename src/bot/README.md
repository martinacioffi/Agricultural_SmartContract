## Pacman

A [DialogFlow](https://dialogflow.com) chatbot for creating agricultural smart contracts.

### Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

In order to build and deploy this chatbot on your local machine, you will need Python 3.6 and a Google account.
Also, since DialogFlow does not work on localhost, you will need Ngrok (which can be downloaded and installed [here](https://ngrok.com/download)) or a similar tunnelling proxy in order to use webhooks.

#### Installing 

Following are the steps that need to be followed in order to create the DialogFlow agent that will communicate with the Python code contained in this repository:
- go to the DialogFlow [login page](https://dialogflow.cloud.google.com/#/login) and log in with your Google account;
- in the top right corner, select "Go to Console" and create a new agent;
- click on the gear next to your agent name, and set the Project ID as environmental variable by running ```export PROJECT_ID="your_project_id" ```; note for **Windows users**: replace `export` with `set` both here and in the last instruction;
- go to the [create service account](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.215926871.-1742798903.1541256042) page of the GPC Console; from the **Service account** list, select **New service account**; in the **Service account** name field, enter a name; and from the **Role** list, select **Project > Owner**. Finally, click **Create** to download the JSON file containing your key to your computer;
- store the above file in a safe location, and set the environmental variable to provide authentication credentials to your application code as follows:
 ```export GOOGLE_APPLICATION_CREDENTIALS="path/to/your_credentials.json" ``` . 
 
 You can now create the chatbot by running
 
 ````python3 -m bot_src.create_chatbot.create_pacman````
 
 You then need to fire up ngrok by cd'ing into the right folder where you unzipped it, and run
 
 ````./ngrok http 5000````
 
 Finally, go back to the DialogFlow console, click on Fulfillment, enable Webhook and copy and paste the second link displayed by ngrok in the URL section, followed by ``/webhook`` and save.
 You can now interact with your newly created chatbot by running 
 
  ```` python3 -m bot_src.server.main.py````
  
 and visiting [localhost](http://127.0.0.1:5000/). 
 
 