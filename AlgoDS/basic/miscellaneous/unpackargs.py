def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"
    
dict1={"bad":'great',"voltage":'One hundred',"fireway":'train','good':'bad'}    
# Unpacking Argument Lists
# Position matters, number of elements matters
parrot(*dict1)