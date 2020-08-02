import abc
from abc import ABC, abstractmethod 
  
class Scrapper(ABC): 
    def __init__(self, name):
        self.name = name
    
    @abc.abstractproperty
    def propName(self):
        return self.name

    @abstractmethod
    def base_url(self): 
        pass
    
    @abstractmethod
    def sub_domain_url(self): 
        pass

    @abstractmethod
    def html_xml_node(self): 
        pass

    @abstractmethod
    def xpath_expression(self): 
        pass

    @abstractmethod
    def base_test(self):
        print("The enrichment")