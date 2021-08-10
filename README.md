# Simple-ChatBot

This is a simple ChatBot made using Python and Tensorflow / Keras.
It's not a super smart chatbot. It can only learn to recognize user added Patterns in the file 'intents.json'.

## Setup
Setup is easy, Python Version 3.6 is recommended, but you may be fine with other versions but just note that you might get errors,
and if you do then simply change your python version to 3.6 and hopefully it will work!

Then run the following command in your terminal:
pip install -r requirements.txt

and boom you're good to go, in any case if you get any erroes, do contact me.

## Train the model
It is very easy to train the model, just run simple-chatbot.py and it will start training the model.

## Interact with your bot
If your training is finished and a new file named 'model.keras' appears in your working directory that means 
you have done everything correctly, now just run the same simple-chatbot.py file to chat with your bot.

## Add your own data
In order to add your own data, open intents.json file and in there add a new dictionary just at the bottom of the existing one in the following format:

{
  "class": "ur_class_name",
  "inputs": ["user inputs for your bot"],
  "outputs": ["bot outputs"]
}

Make sure that it's syntax is correct and save the file.
After this, just delete the model file and run simple-chatbot.py and it should start training the model.
