import itertools

lista = [1,2,3]

# use itertools to get list permutations
for stuff in itertools.permutations(lista, 3):
    print stuff
    
# ===>
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)

# use itertools to get a list's combinations, k indicates the length
for stuff in itertools.combinations(lista, 2):
    print stuff
# ==> 
# (1, 2)
# (1, 3)
# (2, 3)


