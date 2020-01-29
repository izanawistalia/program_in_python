word_count = {}

sentence = "i like name nurarihyon because it is the name of the character in a manga i like"
words = sentence.split()
print(words)
for word in words:
    if(word_count.get(word) != None):
        word_count[word] +=1
    else:
        word_count[word] = 1

print(word_count)