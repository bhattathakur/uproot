#opening the text file which contains the pdg values for t->Scan("pdg","pro==6210 && pdg>50e6") 6210 is for radioactive decay

filename="pdgall.txt" #file name
#writing the results in a file
writefile=open("allpdg.dat","w")
counts=dict()
with open(filename) as f:
    pdgdata=f.read().strip().split("\n")
    for word in pdgdata:
        word=int(word);
        counts[word]=counts.get(word,0)+1
    print("Printing the words and counts\n") 
    for key,value in counts.items():
        print(key,value)
#sorting the dictionary values based on the values in ascending order and 
#put in order
#asceding=[k:v for k,v in sorted(counts.items(),key=lambda item:item[1])]
ascending=sorted(counts.items(),key=lambda x:x[1],reverse=True)
print("ascending order based on values:\n",ascending)
for i in range(len(ascending)):
    writefile.writelines(str(ascending[i][0])+"\t"+str(ascending[i][1])+"\n")
    print("{0:<20d}{1:<20d}".format(ascending[i][0],ascending[i][1]))
#writefile.writelines(ascending)
writefile.close()


#display first 20 pdg data
print("first 20 pdg values\n")
print(pdgdata[:20],end="\n");

#sort the pdg from smaller to bigger value
pdgdata=[int(i) for i in pdgdata]
sortedpdg=sorted(pdgdata);
#sortedpdg=[sorted(int(i))for i in sortedpdg]
#display first 20 sorted pdg data
print("first 20 sorted pdg values\n")
print(sortedpdg[:20],end="\n");
#display first 20 unique pdg data
print("first 20 unique pdg values\n")
print(set(sortedpdg))
print("unique pdg values:",len(set(sortedpdg)))
