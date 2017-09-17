import urllib2
from bs4 import BeautifulSoup

targetUrl = 'http://www.yamibuy.com/cn/'

def analyzeURL(url1):
    req = urllib2.Request(url1, headers={'User-Agent' : "Magic Browser"})
    webpage = urllib2.urlopen(req)
    pageContent = webpage.read()
    
    soup = BeautifulSoup(pageContent, "lxml")
    
    searchBar = soup.findAll('input', {'name':'keywords'})
    
    print 'Analyzing URL complete.'
#     print searchBar
    
    # extracted text from placeholder
    return searchBar[0]["placeholder"]

if __name__ == "__main__":    
    # call yamibuy website and retrieve coupon related information
    couponPool = set()
    repCounter = 20
    prevLen = -1
    
    while True and repCounter > 0:
        prevLen = len(couponPool)
        couponInfo = analyzeURL(targetUrl) 
        # print couponInfo
        couponPool.add(couponInfo)
        if len(couponPool) == prevLen:
            repCounter -= 1
        
        
    print "found " + str(len(couponPool)) + " coupons."
    print "========Coupons========"
    print '\n'.join(couponPool)
    print "======================="