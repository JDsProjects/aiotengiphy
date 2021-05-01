import aiohttp, asyncio
from contextlib import contextmanager

__version__ = "0.1.0"

class GiphyGif:
    def __init__(self, data):
        self.url = data["url"]
        self.embed = data["embed_url"]
        self.id = data["id"]
        self.created_at = data["create_datetime"]
        

class GiphySearch:
    def __init__(self, api_key : str, query : str, session, safe_search=None):
        self.api_key = api_key
        self.query = query
        self.session = session
        self.params = {"api_key": self.api_key, "q": self.query, "rating": safe_search}
        
    async def search(self):
        async with self.session as session:
            async with session.get("https://api.giphy.com/v1/gifs/search", params=self.params) as resp:
                data = await resp.json()
                return GiphyImage(data)
            await session.close()
        
    async def __aexit__(self):
        pass
        
    async def __aenter__(self):
        await self.search()   
        return self             
        
class Client:
    """
    A class for Giphy, Tenor.
    """
        
    class Giphy:
        """
        A class for Giphy API.
        """
        def __init__(self, api_key : str = None):
            self.api_key = api_key        
        
        @contextmanager
        async def search(self, query : str, *, safe_search=None):
            if safe_search:
                pg = "pg-13"  
            else:
                pg = None  
            async with GiphySearch(api_key=self.api_key, query=query, safe_search=pg) as resp:
                return resp                                                                                                                                             
