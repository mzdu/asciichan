# Brief Tour of the Standard Library

# Internet Access
import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print line


# Note that the example needs a mailserver running on localhost.
#===============================================================================
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
# 
# Beware the Ides of March.
# """)
# server.quit()
#===============================================================================


# !!! Dates and Times
# dates are easily constructed and formatted
from datetime import date
now = date.today()
print now
# 2013-05-23

print now.strftime("%m-%d-%y. %d %B %Y is a %A on the %d day of %B.")
# 05-23-13. 23 May 2013 is a Thursday on the 23 day of May.

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print age.days  #17828


# data compression
import zlib
s = 'witch which has which witches wrist watch'
print len(s)  #41

t = zlib.compress(s)
print len(t)  #37

print zlib.decompress(t)   # 'witch which has which witches wrist watch'

print zlib.crc32(s)  #226805979


# Performance Measurement
from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.57535828626024577   real time:226805979
Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.54962537085770791   real time:0.213738718364
# More: http://docs.python.org/2/library/timeit.html#module-timeit

print '---------------------'

# Quality Control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
#  TestResults(failed=0, attempted=1)



# Mutli-thread

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'Finished background zip of: ', self.infile

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print 'The main program continues to run in foreground.'

background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'

# Logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')