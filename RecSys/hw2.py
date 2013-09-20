import csv

movieSet=[]

with open('hw2data.csv','rU') as f:
    reader = csv.reader(f)
    for row in reader:
        movieSet.append(row)
print 'zzzzzzzzzzzzzzzzzzzzz'        
       
# calculate mean rating
# [[movie name, mean rating],[],[],...]
meanRating=[]
movieCounter = 0
userCounter = 0
numMovies = len(movieSet[0]) - 1 
numUsers = len(movieSet) -1 

print 'numMovies: ' + `numMovies`
print 'numUsers: ' + `numUsers`

#constructor
print 'constructor'
#tempList = [MovieName + 20 users' rating]
#meanRating is the set of tempList = [[movie1,1,2,3...],[movie2,2,1,4,...],[movie3,1,1,1,...],...]
moviewithratings=[''] * (numUsers + 1)
moviecollection = [''] * numMovies

test=[['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

print len(test[0])
# only keep the names of movies and their votes
dataset = movieSet
print dataset
'''
for line in dataset:
    #print 'start of lines...' + str(userCounter)
    for column in line[1:]:
        
        print 'start of column ' + str(movieCounter)
        
        moviewithratings[movieCounter] = column
        
        print moviewithratings
        
        moviecollection[userCounter] = moviewithratings
        print moviecollection
        
        movieCounter = movieCounter + 1
    
    movieCounter = 0
    userCounter = userCounter + 1
    
    if userCounter > 19:
        break
    
print moviecollection
'''
for i in range(21):
    for j in range(21):
        test[j][i]=dataset[i][j]
        
print test      

print test[1] 

counter0 = 0
sum1 = 0

for k in range(1,21):
    print 'k is ' + str(k)
    
    for number in test[k][1:]:
        if number == '':
            counter0 += 1
            continue
        else:
            sum1 = sum1 + int(number)

print sum1
print counter0
validVotes = 21 - counter0
print validVotes
deliv1 = float(sum1) / float(validVotes)
print deliv1