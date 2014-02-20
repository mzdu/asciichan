class dx:
    dxx = 0
    
    def __init__(self,name):
        self.name = name
        print name,'is already!'
        dx.dxx += 1
        
    def __del__(self):
        print self.name,'will be delete!'
        dx.dxx -= 1
        if dx.dxx == 0:
            print 'bye~'
        else:
            print '%d left' % dx.dxx
            
    def hi(self):
        print 'my name',self.name
    def many(self):
        if dx.dxx == 1:
            print 'only one'
        else:
            print 'we have %d' % dx.dxx

dt = dx('test')
dt.hi()
dt.many()

x = dx('text')
x.hi()
x.many()

dt.hi()
dt.many()

