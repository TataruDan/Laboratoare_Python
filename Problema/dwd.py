from itertools import permutations
import rowordnet as rwn
import enchant
from googletrans import Translator
wn = rwn.RoWordNet()
word = input("Introdu cuvintul : ")

letter = [x.lower() for x in word]
translated_word = []


for y in list(permutations(letter)):
    z = "".join(y)
    translated_word.append(z);


translator = Translator()

print("Before translate : ")

for i in translated_word:
    print(i)

print("After translate : ")
for index,word in enumerate(translated_word):
    translated_word[index] = translator.translate(word, dest="en")

for i in translated_word:
    print(i.text)

print("Changed : ")
result = []
dict = enchant.Dict("en_US")
for index,word in enumerate(translated_word):
    if " " in word:
        continue
    if not dict.check(word):
        translated_word.remove(index)
    else:
        continue
for i in translated_word:
    print(i)

