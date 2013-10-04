"""
Main Simulation Steps
Here is the main simulation.

Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
For each second (currentSecond):
Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
If the printer is not busy and if a task is waiting,
Remove the next task from the print queue and assign it to the printer.
Subtract the timestamp from the currentSecond to compute the waiting time for that task.
Append the waiting time for that task to a list for later processing.
Based on the number of pages in the print task, figure out how much time will be required.
The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
After the simulation is complete, compute the average waiting time from the list of waiting times generated.
"""
# Not finished
import Queues
import Printer
import Task

import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer.Printer(pagesPerMinute)
    printQueue = Queues.Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)