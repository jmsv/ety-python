import ety

data = ety.data.etyms

print(len(data))
sen = 'international shipping of products including games books and movies'
sen = sen.split(' ')

for word in sen:
    w1 = ety.word.Word(word)
    print(ety.EtyTree(w1))