# In this problem to check Longest compound words match given Input_01.txt,Input_02.txt string words. 
# To find the Longest compund words and second compound words to identify the sting are Longest compound words="ratcatdogcat".
# In this code to identify the longest word Concatenated from 4 words=['rat', 'cat', 'dog', 'cat'].
# And Second Longest Compound Word="catsdogcats" to Concatenated from 3 words=['cats', 'dog', 'cats'].
# The no. of matches are compond words. 
import os
import sys
class Node:
    def __init__(self,L=None,T=False):
        self.L=L
        self.T=T
        self.child={}
class Trie:
    def __init__(self):
        self.root=Node()
        self.count={}
    def Add(self, word):
        K=self.root
        for L in word:
            if L not in K.child:
                K.child[L]=Node(L)
            K=K.child[L]
        K.T=True
    def __contains__(self, word):
        K=self.root
        for L in word:
            if L not in K.child:
                return False
            K=K.child[L]
        return K.T
    def merge(self, word):
        if not word:
            return 0,[]
        if word in self.count:
            return self.count[word]
        K = self.root
        for index, L in enumerate(word):
            if L not in K.child:
                return 0,[]
            K=K.child[L]
            if K.T:
                suffix=word[index + 1:]                           
                suffix_count,suffix_list=self.merge(suffix)  
                self.count[suffix]=suffix_count, suffix_list     
                if suffix_count:                                    
                    return 1+suffix_count,[word[:index + 1]]+suffix_list 
        return K.T,[word]
    def getCompound(self, word):
        merge_num,merge_list=self.merge(word)
        return merge_num>1,merge_num,merge_list
def load(data):
    words=[]
    trie=Trie()
    with open(data, 'r') as f:
        for line in f:
            word=line.strip()
            trie.Add(word)
            words.append(word)
    return trie,words
def processList(compoundList):
    compoundList.sort(key = lambda tup: len(tup[0]), reverse=True)
    return compoundList
def getCompoundList(trie, words):
    compound=[]
    for word in words:
        isValid,num,dlist=trie.getCompound(word)
        if isValid:
            compound.append((word, num, dlist))
    return compound
def dataset(data='Input_02.txt'):
    trie, words=load(data)
    compoundList=processList(getCompoundList(trie, words))
    longestWord=compoundList[0][0]
    secondLongestWord=compoundList[1][0]
    if len(longestWord):
        print("Longest compound word :\t\""+longestWord+"\"")
    else:
        print("No largest compound words")
    if len(secondLongestWord):
        print("Second compound word :\t\""+secondLongestWord+"\"")
    else:
        print("No second largest compound words")
    print("Number of compound words is "+str(len(compoundList)))
    return trie,words,compoundList
def main(argv):
    data=sys.argv[1]
    if not os.path.isfile(data):
        print("Could not find\""+data +"\"")
        sys.exit()
    dataset(data)
if __name__ == "__main__":
    main(sys.argv)
