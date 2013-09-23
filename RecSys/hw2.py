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


for i in range(21):
    for j in range(21):
        test[j][i]=dataset[i][j]
        
print test      

# this is the first dataset
print 'first data set'
print test[1] 


# there are twenty movie data sets from test[1] to test[21]

validVotes = 0

for number in range(1,21):
    print '----set[' + `number` + ']----'
    # counter0 calculates the number of void element
    counter0 = 0
    # counter1 calculates the number of 4+
    counter1 = 0
    sum1 = 0
    mean1 = 0
    

    # calculate the mean value here
    for element in test[number][1:]:
        #print element
        if element == '':
            counter0 += 1
        
        elif int(element) >= 4:
            print 'bingo 4+ ' + 'element is ' + element
            counter1 += 1
        
        else:
            sum1 = sum1 + int(element)
    print 'sum1 is ' + `sum1`
    print 'counter of void is '+ `counter0`
    validVotes = 20 - counter0
    print 'valid votes ' + `validVotes`
    mean1 = float(sum1) / validVotes
    print 'Mean value is ' + str(mean1)
    
    # output of rating of 4+
    print 'counter of 4+ is ' + `counter1`
    print 'rate of 4+ is ' + str(float(counter1)/validVotes)

    
# here we calculate the Association with StarWars IV
# counter2 calcuates the number of users who rated sw also rate another movie
counter2 = 0 

# num1 controls the number of row
for num1 in range(2,21):
    # num controls the number of line
    for num in range(1,21):
        
        if movieSet[num][1] != '' and movieSet[num][num1]!='':
            counter2 += 1
        else:
            continue
            
    asRate = float(counter2)/16
    print 'Association Rate of movie[' + str(num1) + '] is ' + str(asRate)
    asRate = 0
    counter2 = 0

        
