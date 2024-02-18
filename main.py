import requests as req
import string

letters = list(string.ascii_lowercase)
other_letters = []
central_letter = 0
while central_letter not in letters:
    central_letter = input("Enter the central letter: ")

for i in range(6):
    temp_letter = 0
    while temp_letter not in letters:
        temp_letter = input("Enter side letter #{num}: ".format(num=i+1))
        other_letters.append(temp_letter)

# 4-letter words
for letter1 in other_letters:
    word = letter1
    for letter2 in other_letters:
        word2 = word + letter2
        for letter3 in other_letters:
            word3 = word2 + letter3
            for letter4 in other_letters:
                word4 = word3 + letter4
                response = req.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word4)
                if response.status_code == 200:
                    print(word4)