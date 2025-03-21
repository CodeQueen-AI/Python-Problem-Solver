# Write a Python program that takes a sentence as input and reverses the entire sentence
sentence = input("Enter a Sentence: ")  
reversed_sentence = ' '.join(sentence.split()[::-1])  
print("Reversed sentence:", reversed_sentence)


