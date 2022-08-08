# Create a dictionary and take input from the user and return the meaning of the word from the dictionary

dictionary = {"patience": "धैर्य", "stubborn": "ज़िद्दी", "nightmare": "बुरा सपना"}
word = input("Enter the word: ")
mean = dictionary.get(word)
print(f"The meaning of {word} is {mean}")
