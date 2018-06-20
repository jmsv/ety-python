import ety
from random import choice


data = ety.data.etyms

print(len(data))
sen = 'international shipping of products including games books and movies'
sen = sen.split(' ')

'''
for word in sen:
    w1 = ety.word.Word(word)
    print(ety.EtyTree(w1))
'''

#print(ety.random_word())
print(ety.random_word('eng'))
print(ety.origins('aerodynamic'))
#return Word(choice(list(data[lang])), lang)
