# builder.py access and download the specified webpage, then resolve the html code with BeautifulSoup
# find out and save the lottery data in xx.txt files.

import urllib2
import pickle
from bs4 import BeautifulSoup

url05 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2005'
url06 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2006'
url07 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2007'
url08 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2008'
url09 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2009'
url10 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2010'
url11 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2011'
url12 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2012'
url13 = 'http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2013'

urltuple = (url05,url06,url07,url08,url09,url10,url11,url12,url13)

def analyzeURL(url1):
    req = urllib2.Request(url1, headers={'User-Agent' : "Magic Browser"})
    webpage = urllib2.urlopen(req)
    pageContent = webpage.read()
    
    soup = BeautifulSoup(pageContent)
    
    red_part = soup.findAll('span', {'class':'STYLE13'}) 
    blue_part = soup.findAll('span',{'class':'STYLE12'})
    
    print 'Analyzing URL complete.'
    return red_part, blue_part

#if len(red_part) == len(blue_part):
#    print 'yes'

def constructNewList(part1, part2):
    rootlist = []
    sublist = []
    
    for counter in range(len(part1)):
        a1 = str(part1[counter])
        b1 = str(part2[counter])
        
        sublist.extend([a1[22:24],a1[26:28],a1[30:32],a1[34:36],a1[38:40],a1[42:44],b1[22:24]])
        rootlist.append(sublist)
        sublist = []
    
    print 'List construction complete!'    
    return rootlist

def lancher(url):        
    red_part, blue_part = analyzeURL(url)
    list1 = constructNewList(red_part,blue_part)
    
#    f= open('./data/'+url[-2:]+'.txt','w')
#    f.write(str(list1))
#    f.close()
    
    # Use pickle to save the data structure
    afile = open(r'./data/'+url[-2:]+'.pkl', 'wb')
    pickle.dump(list1, afile)
    afile.close()
    
    
    
    print 'Start Launcher.'

def buildData():
    for url in urltuple:
        lancher(url)

    print 'Data building complete!'
    

buildData()