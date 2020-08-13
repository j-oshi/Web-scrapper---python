import abc
from abc import ABC, abstractmethod 
  
class Scrapper(ABC): 
    def __init__(self, name):
        self.name = name

    # @abstractmethod
    def url_address(self): 
        pass

    # @abstractmethod
    def get_web_content(self): 
        pass