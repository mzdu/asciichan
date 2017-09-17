import urllib2
from bs4 import BeautifulSoup

newLinkPool = []

url = 'https://discuss.leetcode.com/user/caikehe?page='
urls = [url + str(i) for i in xrange(76, 75, -1)] # till 77
with open('keheAnswers.html', 'w') as f:
    for url in urls:
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        webpage = urllib2.urlopen(req)
        pageContent = webpage.read()
         
        soup = BeautifulSoup(pageContent)
         
        links = soup.findAll('a', {'class':'topic-title'})
        sublinks = [link['href'] for link in links] 
        # print stuff
        
        # [u'/post/167259', u'/post/51280', u'/post/51273', u'/post/51268', u'/post/49753', u'/post/49749', u'/post/47067', u'/post/47066', u'/post/46998', u'/post/46861']
        
        # one link to one topic
        postBase = 'https://discuss.leetcode.com/'
        newLinks = [postBase + subLink for subLink in sublinks]
        
        for newLink in newLinks:
    #         newLink = 'https://discuss.leetcode.com/post/167259'
            req = urllib2.Request(newLink, headers={'User-Agent' : "Magic Browser"})
            webpage = urllib2.urlopen(req)
            pageContent = webpage.read()
            
            soup = BeautifulSoup(pageContent)
            
            links = soup.findAll('span', {'itemprop':'title'})
            # get text from span section
            title = links[-2].text
            topic = links[-1].text
            # stuff = [link['href'] for link in links] 
            print title, topic, newLink
            newLine = '<br/><strong>' + title + '</strong>, <span>' + topic + '</span>, <a href="' + newLink + '">' + str(newLink) + '</a> <br />'
            f.write('\n' + newLine)

