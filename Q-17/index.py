#Take a string as input and count the number of vowels and consonants in it
text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print("Vowels:", vowel_count, "Consonants:", consonant_count)
