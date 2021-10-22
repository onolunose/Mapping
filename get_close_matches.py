import json
data = json.load(open("theophilus/sample2.json"))
from difflib import get_close_matches

def translator(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        yeah = raw_input('Type Y if you mean %s or N if you mean NO  '% get_close_matches(word, data.keys())[0])
        if yeah == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yeah =='N':
            return ' This word does not exist'
        else:
            return ' We do not understand your entry'
        
    else:
        return 'This %s does not exist' % word
word = raw_input('Enter something Please: ')
output = translator(word)
if type(output)== list:
    for item in output:
        print item
else:
    print output
