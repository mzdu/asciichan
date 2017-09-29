list1 = ['tic','tac','toe']
color = ['Red','Green','Blue']
others = ['air','dust']

print zip(list1,color)    
#[('tic', 'Red'), ('tac', 'Green'), ('toe', 'Blue')]

print zip(list1,color,others)
#[('tic', 'Red', 'air'), ('tac', 'Green', 'dust')]