"""
Hot Potato Game Rules: children line up in a circle and pass an item from neighbor to neighbor as fast as they can. 
At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. 
Play continues until only one child is left.
"""

import Queues

def hotPotato(nameList,count):
    num = 0
    nameQ = Queues.Queue()
    
    while nameList != []:
        tempName = nameList.pop(0)
#        print tempName
        nameQ.enqueue(tempName)
        # The name queue is ready
        
    while nameQ.size()>=1:
            currentName = nameQ.dequeue()
            print 'currentName',currentName
            num = num + 1
            
            if num == count:
                print currentName,'is out'
                num = 0
                continue
            else:
                nameQ.enqueue(currentName)
            
            if nameQ.size() == 1:
                print currentName,'is the Winner'
                return currentName
            

hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)        