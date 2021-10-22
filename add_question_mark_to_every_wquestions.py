def construct_sentence(phrase):
    interrogation = ("what", "how", "when","where")
    capital= phrase.capitalize()
    if phrase.startswith(interrogation):
        return '{}?'.format(capital)
    else:
        return '{}.'.format(capital) 
new_user_input = []        
while True:
    user_input= raw_input()
    if user_input == '-':
        break
    else: 
        new_user_input.append(construct_sentence(user_input))
print (' '.join(new_user_input))

