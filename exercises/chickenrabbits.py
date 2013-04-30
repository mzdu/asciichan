# solve chicken rabbits in cage problem

def func1(legs, heads):
    num_chicken = 0
    num_rabbit = 0
    while True:
        num_rabbit = heads - num_chicken
        if num_chicken * 2 + num_rabbit * 4 == legs:
            return (num_chicken, num_rabbit)
        
        else:
            if num_chicken <= heads:
                num_chicken += 1
            else:
                print "No answer."
                return False


print func1(56, 20)
    