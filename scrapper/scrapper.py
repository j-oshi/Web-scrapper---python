import abc
from abc import ABC, abstractmethod 
  
class Scrapper(ABC): 
    def __init__(self, name):
        self.name = name
    
    # @abc.abstractproperty
    # def propName(self):
    #     return self.name

    @abstractmethod
    def get_web_content(self): 
        pass
    
    @abstractmethod
    def get_html_content(self): 
        pass
    
    @abstractmethod
    def get_query_list(self):
        pass
    # @abstractmethod
    # def html_xml_node(self): 
    #     pass

    # @abstractmethod
    # def xpath_expression(self): 
    #     pass

    # @abstractmethod
    # def base_test(self):
    #     print("The enrichment")