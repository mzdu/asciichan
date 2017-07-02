import urllib2
from bs4 import BeautifulSoup

targetUrl = 'http://www.yamibuy.com/cn/'

def analyzeURL(url1):
    req = urllib2.Request(url1, headers={'User-Agent' : "Magic Browser"})
    webpage = urllib2.urlopen(req)
    pageContent = webpage.read()
    
    soup = BeautifulSoup(pageContent)
    
    searchBar = soup.findAll('input', {'name':'keywords'})
    
    print 'Analyzing URL complete.'
#     print searchBar
    
    # extracted text from placeholder
    return searchBar[0]["placeholder"]

if __name__ == "__main__":    
    # call yamibuy website and retrieve coupon related information
    couponPool = set()
    repCounter = 1
    
    while True:
        couponInfo = analyzeURL(targetUrl) 
        
        if couponInfo not in couponPool:
            couponPool.add(couponInfo)
        else:
            repCounter -= 1
            if repCounter == 0:
                break
        print couponInfo
        
        
    print couponPool