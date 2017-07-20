from __future__ import print_function
import math
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

# s1, s2, s3 are in lexicon
s1 = "the process by which some nations enrich themselves through political and economic control of other nations"
s2 = "the process by which one nation takes over another nation, usually for the purpose of exploiting its labor and natural resources"
s3 = "a patriarchal culture in which male violence and rape are tolerated"
s4 = "the part of the economy that draws raw materials from the natural environment"
s5 = "a social culture that provides an environment conducive to rape"
s6 = "the ways in which people construct their sexual identity, attraction, and relationships, including the norms governing sexual behavior"
# target
s7 = "the ways in which people think about, and behave toward, themselves and others as sexual beings"



lexicon = [s1, s2, s3, s4, s5, s6, s7]

# How to convert sentences into vectors??
# S1: create a matrix to calculate the term frequency
# use defaultdict(list) calculate the frequency and sort by key, then measure the distance
# {sentence: {word: frequency}  }
# the number of keys is the length of verctor

# preprocessing, tokenize sentence
import re
tokenizedLexicon = []
for sentence in lexicon:
    # split on spaces, and on commas and periods that aren't surrounded by numbers
    tokenizedLexicon.append(re.split(r" |(?<![0-9])[.,](?![0-9])", sentence))
    
# print(tokenizedLexicon)

from collections import defaultdict
lexiconStat = defaultdict(lambda: defaultdict(int))
# wordPool
wordPool = set()

i = 0
while i < len(tokenizedLexicon):
    print("sentence output:")
    print(tokenizedLexicon[i])
    # tokenize word from sentence
    for word in tokenizedLexicon[i]:
        # start counting
        lexiconStat[i][word] += 1
        if word not in wordPool and word:
            wordPool.add(word)
    i += 1
# print("lexiconStat")
# print(lexiconStat)

#OUTPUT: 
# {0: {word1: count01, word2: count02}}
# {1: {word3: count13, word2: count12, word4: count14}}
# {2: {word1: count21}}

# vector length
sortedWordPool = sorted(wordPool)
print("sortedWordPool")
print(sortedWordPool)
# """
# sortedWordPool
# ['a', 'and', 'another', 'are', 'by', 'control', 'culture', 'economic', 'enrich', 'exploiting', 'for', 'in', 'its', 'labor', 'male', 'nation', 'nations', 'natural', 'of', 'one', 'other', 'over', 'patriarchal', 'political', 'process', 'purpose', 'rape', 'resources', 'some', 'takes', 'the', 'themselves', 'through', 'tolerated', 'usually', 'violence', 'which']
# """

#wordPool = {word1, word2, word3, word4}
vectorSpace = defaultdict(list)
tempVector = []
# {
# 0:[count01, count02, 0, 0],
# 1:[0, count12, count13, count14],
# 2:[0, count21, 0, 0],
# }

for tokenizedSentence in lexiconStat:
    # print("lexiconStat[tokenizedSentence]")
    # print(lexiconStat[tokenizedSentence])
    # defaultdict(<type 'int'>, {'a': 1, 'patriarchal': 1, 'and': 1, 'tolerated': 1, 'violence': 1, 'culture': 1, 'are': 1, 'which': 1, 'in': 1, 'male': 1, 'rape': 1})
    
    for word in sortedWordPool:
                print("word in sortedWordPool")
                print(word)
                print(lexiconStat[tokenizedSentence][word])
                tempVector.append(lexiconStat[tokenizedSentence][word])
                
    # print("tempVector")
    # print(tempVector)
    vectorSpace[tokenizedSentence] = tempVector
    # reset tempVector
    tempVector = []
    
print("vectorSpace")
print(vectorSpace)
    
# calculate the cosine distance
i = 0
resScore = -1
resIdx = 0

while i < len(lexicon) - 1:
    score = cosine_similarity(vectorSpace[i], vectorSpace[6])
    if score >= resScore:
        resIdx = i
        resScore = score
    # problem: what if we encounter out of vocabulary situation?
    i += 1

print("The best match found, and the score is", resScore)
print("Input sentence: ", lexicon[-1])
print("Best match is: ", lexicon[resIdx]) 