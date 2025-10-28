# * First you go to the working directory of the project
# * python -m venv venv_name

import requests

word = input("Enter the word: ")

data = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()

print('Searched word: ', data[0]['word'])
print('Phonetic Sound: ', data[0]['phonetic'])

# definitions = data[0]['meanings'][0]['definitions']
meanings = data[0]['meanings']


for meaning in meanings:
    definitions = meaning['definitions']

    for definition in definitions:
        print('Definition: ', definition['definition'])
        print('Example: ', definition.get('example', ''))

