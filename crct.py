from textblob import TextBlob
words = input("type your word ")
corrected_word = TextBlob(words)

print("Wrong word :", words)
print("Corrected Word is :", corrected_word.correct())
