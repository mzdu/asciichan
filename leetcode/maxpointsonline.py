"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
# needs to be revised.... 
#Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
 
from collections import namedtuple
 
class Solution:
    # @param points, a list of Points
    # @return an integer
     
    # create a namedtuple to store those points
     
 
     
    def maxPoints(self, points):
         
        kinfo = namedtuple('kinfo',['points', 'kvalue'])
        kinfos = []
        numPoints = len(points)
        
        idx1 = 0
        idx2 = 1
             
        while idx1 < numPoints - 1:
            
            while idx2 < numPoints:
                if (points[idx2].x - points[idx1].x) == 0:
                    if (points[idx2].y - points[idx1].y) == 0:
                        k = False
                    else:
                        k = 'max'
                    
                else:
                    k = float((points[idx2].y - points[idx1].y))/float((points[idx2].x - points[idx1].x))
                kinfo = ((str(idx1),str(idx2)), k)
                kinfos.append(kinfo)
                
                idx2 = idx2 + 1
            
            idx1 = idx1 + 1
            idx2 = idx1 + 1
             
        
        print 'kinfos',kinfos
        
        pointsDict = dict()
        pointSet = []
         
         
         
        for kinfo in kinfos:
            
            #check if the kvalue had been saved before
            try:
                pointSet = pointsDict[kinfo[1]]
                pointSet.append(kinfo[0])
                pointsDict[kinfo[1]] = pointSet
            
            except:
                pointSet.append(kinfo[0])
                pointsDict[kinfo[1]] = pointSet
                
            pointSet = []
          
        maxlen = 0
        line = []
        c1 = 0
        c2 = 1
        c3 = 0
        
        pset = pointsDict.values()
        
        print pset
        
        for pp in pset:
             
            if pp == []:
                pass
            else:
                #avoid cycle
                pp.sort()
                # detect how many lines are equal to each other
                
                while c1 < len(pp)-1:
                    c3 = c1
                    line.append(pp[c3])
                    while c2 < len(pp):
                        if pp[c3][0] == pp[c2][0]:
                            c2 = c2 + 1
                        else:
                            if pp[c3][1] == pp[c2][0]:
                                line.append(pp[c2])
                                
                                c3 = c2
                                c2 = c3 + 1
                            else:
                                c2 = c2 + 1
                        
                    if len(line) > maxlen:
                        maxlen = len(line)
                        print 'maxline', line
                    else:
                        pass    
                    
                    line = []
                        
                    c1 = c1 + 1
                    c2 = c1 + 1
        
        return maxlen
            
        
        
        
testcase = [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)]        

points = []
# testcase = [(0,0),(1,1),(0,0)] 

for case in testcase:
    points.append(Point(case[0],case[1]))
    

# pa = Point(12,12) #0
# pb = Point(1,8) #1
# pc = Point(9,7) #2
# pd = Point(1,2) #3
# pe = Point(3,3) #4
# pf = Point(6,6) #5
# pg = Point(5,5) #6
# points = [pa, pb, pc, pd, pe, pf, pg]

#print points[0].x

sol = Solution()
print sol.maxPoints(points)
