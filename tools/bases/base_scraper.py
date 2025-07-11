from abc import ABC, abstractmethod

class BaseScraper(ABC):
    
    @abstractmethod
    def scrape(self, url: str) -> str:
        """scrape the url and return the data"""
        raise NotImplementedError