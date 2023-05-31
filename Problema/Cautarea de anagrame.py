import requests
from itertools import permutations
from bs4 import BeautifulSoup

def check_word(word):
    URL = "https://dexonline.ro/definitie/" + word
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    response = soup.find("h3", class_="")

    if "Niciun rezultat pentru" in response.text.strip() or "nu este în dicționar. Iată câteva sugestii:" in response.text.strip():
        return
    else:
        return word



word = input("Introdu cuvintul : ")
initial_word = word

letter = [x.lower() for x in word]
words = []

for y in list(permutations(letter)):
    z = "".join(y)
    words.append(z);

results = []
for word in words:
    results.append(check_word(word))
print("Anagramele pentru cuvintul " + initial_word + " sunt : ")
results = [x for x in results if x is not None]
for word in results:
    print(word)


