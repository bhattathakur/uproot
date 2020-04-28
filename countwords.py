sentence=input("Ente th sentence to count the respective words in it\n")
words=sentence.split()
print("list of words in given sentence\n")
print(words)
#Defining the dietionray to store the words in it
counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1
print("Printing the words and counts\n")
for key,value in counts.items():
    print(key,value)
