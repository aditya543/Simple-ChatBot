import os
import json 
import numpy as np

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model


class Tokenizer:
	def __init__(self, intents_file):
		self.file_path = intents_file
		self.data = None
		self.inputs, \
		self.labels, \
		self.vocab,  \
		self.classes = self.get_data(self.file_path)
		self.vocab_size = len(self.vocab)
		self.n_classes = len(self.classes)

	def encode(self, text):
		output = [0 for i in range(len(self.vocab))]
		for char in text:
			if char in self.vocab:
				output[self.vocab.index(char)] = 1 
		return output

	def training_data(self):
		x_train, y_train = [], []

		for sent in self.inputs:
			x_train.append(self.encode(sent))

		for label in self.labels:
			y_train.append(self.classes.index(label))
		return np.array(x_train), categorize(y_train)

	def get_data(self, file_path):
		inputs, vocab = [], []
		labels, classes = [], []
		index = 0

		with open(file_path, "r") as f:
			self.data = json.load(f)
		
		for intent in self.data["intents"]:
			for inp in intent["inputs"]:
				inputs.append(inp)
				labels.append(intent["class"])
				for char in inp:
					if char not in vocab:
						vocab.append(char)

			if intent["class"] not in classes:
				classes.append(intent["class"])
		return inputs, labels, vocab, classes


def categorize(lst):
	n_classes = max(lst)
	output = []

	for value in lst:
		out = np.zeros(n_classes + 1)
		out[value] = 1
		output.append(out)
	return np.array(output)


def build_model(vocab_size, n_classes):
	model = Sequential()
	model.add(Dense(128, input_shape=(vocab_size,), activation='relu'))
	model.add(Dense(64, activation='relu'))
	model.add(Dense(n_classes, activation='softmax'))

	model.compile(loss='categorical_crossentropy', metrics=['accuracy'],
				  optimizer='adam')
	return model

def train_model():
	x_train, y_train = tokenizer.training_data()
	model = build_model(tokenizer.vocab_size, tokenizer.n_classes)

	model.fit(x_train, y_train, epochs=100, batch_size=128)
	model.save("model.keras")
	inference()

def inference():
	model = load_model("model.keras")
	while True:
		try:
			query = tokenizer.encode(input("User: ").lower())
			output = model.predict(np.array([query]))
			clas = tokenizer.classes[np.argmax(output)]

			for intent in tokenizer.data["intents"]:
				if clas == intent["class"]:
					print(np.random.choice(intent["outputs"]))
		except ValueError:
			print("You may have changed your intents file, \nif you did then delete the model file and run the program again")
			quit()

tokenizer = Tokenizer("intents.json")
if os.path.exists("model.keras"):
	inference()
else: train_model()