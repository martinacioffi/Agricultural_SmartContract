# Agricultural Smart Contract

This project consists in a basic prototype for writing and deploying smart contracts for agricultural insurance on a blockchain.

It allows users to specify several parameters, which may depend, for instance, on one's land's size, where it is located, or which adverse weather condition one wants to insure against; and afterwards creates and deploys a contract on the blockchain. 
As of now, the easiest way to create a contract is by interacting with the Pacman agent, that guides the user through the steps necessary for the whole contract creation.


## Project Organization

This repository is organized in three main folders:
1. [src](src) contains the main functions needed to create and deploy the contract on a simulated blockchain, in [contract.py](src/contract.py), as well as two other sub-folders, that is:
2. [bot](src/bot), which contains: 
    - [create_chatbot](src/bot/create_chatbot), useful to replicate the chatbot on one's local machine;
    - [server](src/bot/server) to interact with it on localhost;
3. [weather](weather/bot), that contains functions useful to obtain the needed weather measures.

Note that, for ease of testing, the bot is now live on [Facebook Messenger](https://www.facebook.com/pacmanweatheragent/?view_public_for=105311567631131). 
However, in order to appreciate all of its functionalities, one needs:
- Test Users' permissions (email me to get those);
- a tunnelling proxy activated in order for webhooks to works. I can turn these on on request, please email me (martina.cioffi@studbocconi.it) and we can agree on a timeframe (8 hours since when it is started) during which webhooks will be active.

## Future Improvements

While the bot was initially developed in order for farmers of developing countries to more easily create a contract by using means they are likely more accustomed to than computers (i.e. phones and in particular Facebook, or any other platform the bot can be deployed on), it would make sense to also have a website from which one can create his of her own smart contract. In that case, the bot would still be accessible through a chat plugin similar to what can be found [here](https://martinacioffi.github.io/projects/).

Moreover, as of now the bot is extremely basic and is not able to sustain complex conversations (i.e. it cannot handle multiple intents, it does not deal well with typos, etc.).
This is indeed *just a prototype*: ideally, the above and several other features should be added in order for the chatbot to successfully carry out its tasks - for instance, one could think of inserting pictures and suggestions in order to help farmers even more understand what they are insuring against. Also, support for different languages - and possibly dialects - should be added.

As of now, an example of a doable conversation with Pacman looks like this:

    Pacman: Hello! How can I help you?
    User: I would like to create a new contract
    Pacman: I can sure help you with that. Can you please start by telling me your full name?
    User: John Doe
    Pacman: Alright, I got your name as John Doe. Where is your farm located?
    User: India, Mumbai, 98765
    Pacman: Okay. I got your farm's address. Can you please tell me your land's size?
    User: 1.5 hectares
    Pacman: Please, specify the weather condition you would like to insure against.
    User: Rainfall
    Pacman: What kind of contract best suits your needs?
    User: Standard
    Pacman: Alright, we can proceed with a standard contract. For which month would you like to insure
            your crops?
    User: May
    Pacman: I am about to create your contract. Do you want to proceed?
    User: CONFIRM
    Pacman: Congrats, you just created a new contract that grants you protection for your crops in 
            Mumbai, starting from May; average precipitation in this month are 32 mm. As soon as the 
            evaluation period will be over, the index will be evaluated and payments to either you or
            the investor who subsidized your contract will be sent out automatically.
    
Note: 
(i) when the options available are not clear, the user - through the Facebook Messenger platform - is shown buttons with the different options to choose from; 
(ii) when the bot states that the contract has been created, this has actually been sent to the blockchain for deployment. 


[Demo](pacmanOK.mov)
## Authors

- [Martina Cioffi](https://github.com/martinacioffi)
- [Luca Ferrario](https://github.com/lucafirefox)
- [Luca Pacchiana](https://github.com/LucaPacchiana)
- [Marco Pettazzi](https://github.com/Marco-Pettazzi)
- [Benedetta Sargentoni](https://github.com/benedettasrg)

