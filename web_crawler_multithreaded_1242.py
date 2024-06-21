'''
1242. Web Crawler Multithreaded

Medium

Given a URL startUrl and an interface HtmlParser, implement a Multi-threaded web crawler to crawl all links that are under the same hostname as startUrl.

Return all URLs obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all URLs from a webpage of a given URL.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.

As shown in the example URL above, the hostname is example.org. For simplicity's sake, you may assume all URLs use HTTP protocol without any port specified. For example, the URLs http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, while URLs http://example.org/test and http://example.com/abc are not under the same hostname.

The HtmlParser interface is defined as such:

interface HtmlParser {
  // Return a list of all urls from a webpage of given url.
  // This is a blocking call, that means it will do HTTP request and return when this request is finished.
  public List<String> getUrls(String url);
}
Note that getUrls(String url) simulates performing an HTTP request. You can treat it as a blocking function call that waits for an HTTP request to finish. It is guaranteed that getUrls(String url) will return the URLs within 15ms. Single-threaded solutions will exceed the time limit so, can your multi-threaded web crawler do better?

Below are two examples explaining the functionality of the problem. For custom testing purposes, you'll have three variables urls, edges and startUrl. Notice that you will only have access to startUrl in your code, while urls and edges are not directly accessible to you in code.


Example 1:


Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]

https://leetcode.com/problems/web-crawler-multithreaded/description/
'''
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

class Solution:
    def __init__(self):
        self.lock = Lock()
        self.queue = collections.deque()
        self.visited = set()
    
    def extractHostName(self, url):
        return '.'.join(url.split('/')[2].split('.')[1:])    
    
    def downloadUrl(self, curr_url):
        next_urls = self.htmlParser.getUrls(curr_url)
        
		# Use Lock to protect shared states.
        with self.lock:
            for url in next_urls:
                if url not in self.visited and self.curr_hostname == self.extractHostName(url):
                    self.queue.append(url)
                    self.visited.add(url)  
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        self.queue.append(startUrl)
        self.curr_hostname = self.extractHostName(startUrl)
        self.visited = {startUrl}
        self.htmlParser = htmlParser
		# Limit to 10 worker threads
        executor = ThreadPoolExecutor(max_workers=10)
        
        while self.queue:
            curr_url = self.queue.popleft()

            url_list = list()
			# Add at least first URL from the queue
            url_list.append(curr_url)

			# If there are still URLs in the queue, add to the list 
            while self.queue:
                curr_url = self.queue.popleft()
                url_list.append(curr_url)
            
            executor_list = list()
			# Execute this batch of threads with threadpool
            for i in range(len(url_list)):
                executor_list.append(executor.submit(self.downloadUrl, (url_list[i])))
                
			# Main thread waiting for the above threads to finish
            for future in executor_list:
                future.result()
        
        # Shutdown ThreadPool executor
        executor.shutdown()
        
        return list(self.visited)
        
