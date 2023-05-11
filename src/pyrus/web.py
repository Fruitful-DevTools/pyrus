from . import *
from bs4 import BeautifulSoup as bs


class Requests:

    def __init__(self, base_url):
        self.base_url = base_url

    def __call__(self, path=None, params=None):
        """Makes a GET request to the specified path.

        Args:
            path: The path to the API endpoint.
            params: A dictionary of parameters to send with the request.

        Returns:
            The response from the API.
        """
        response = rq.get(self.base_url + path, params=params)
        if response.status_code == 200:
            response = ChainMap(json.loads(response.content)["public"], json.loads(response.content)["private"])
            return response
        else:
            print("Error making request:", response.status_code)

"""class Scrape(Requests):

    def __init__(self):
        pass

    def __call__(self):

        pass
        
class MapSite(Requests):

    def __init__(self):
        self.links = set()
        self.public_pages = set()
        self.visited = set()
    
    def __call__(self):
        for url in queue:
            request = Requests(url)
            response = request()
            soup = bs(response.content, 'html5lib')
            self.find_links(soup)

    def find_links(self, soup):
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                self.links.add(href)

    def get_public_pages(base_url):
        public_pages = set()
        visited = set()
        queue = [base_url]
        while queue:
            url = queue.pop(0)
            if url in visited:
                continue
            
            self.visited.add(url)
            
            if urlparse(url).netloc != urlparse(base_url).netloc:
                continue
            
            if url.endswith('.pdf'):
                continue

            response = requests.get(url)

            if response.status_code == 200:
                public_pages.add(url)
                links = get_links(url)
                
                for link in links:
                    
                    absolute_link = urljoin(url, link)
                    
                    if urlparse(absolute_link).scheme in ['http', 'https']:
                        queue.append(absolute_link)
        return public_pages

#class SiteIterator(Requests, MapSite):

    #def __call__():
        #pass
"""