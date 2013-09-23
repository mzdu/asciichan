import pickle


#reload object from file
file2 = open(r'./data/05.pkl', 'rb')
new_d = pickle.load(file2)
file2.close()

#print dictionary object loaded from file
print new_d

for i in range(len(new_d)):
    print new_d[0][6]