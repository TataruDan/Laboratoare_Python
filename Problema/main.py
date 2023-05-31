import random
import requests
from textblob import Word
from googletrans import Translator
import itertools
from PyDictionary import PyDictionary
import rowordnet as rwn


def get_list_of_words():
    response = requests.get(
        'https://svnweb.freebsd.org/base/head/share/dict/web2?view=co',
        timeout=10
    )

    string_of_words = response.content.decode('utf-8')

    list_of_words = string_of_words.splitlines()

    return list_of_words


def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")



words = get_list_of_words()

# random_word = random.choice(words)

translator = Translator()
translation = translator.translate("setca", dest="en")
inserted_word = input("Insert you word : ")
rez = []


print(translation.text)
dictionary=PyDictionary()

checker = translator.translate(translation.text, dest="en")

if(words.count(checker.text) == 0):
    print("This word do not exist in dictionary!")
    exit(0)
else:
    print(["".join(perm) for perm in itertools.permutations(translation.text)])
    list_of_words = ["".join(perm) for perm in itertools.permutations(translation.text)]
    final_result = []
    wn = rwn.RoWordNet()
    print(wn.synsets(literal="astec"))
    for word in list_of_words:
        if not (wn.synsets(word)):
            final_result.append(word);
        else:
            continue
print(final_result)

#
# if(dictionary.meaning(translation.text) != None):
#     print(["".join(perm) for perm in itertools.permutations(translation.text)])
#     list_of_words = ["".join(perm) for perm in itertools.permutations(translation.text)]
#
#     print(list_of_words)
# else:
#     print("This word do not exist!")









