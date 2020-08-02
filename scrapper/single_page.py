from scrapper import Scrapper

class SinglePage(Scrapper): 
    instances = []
    def __init__(self, name):
        self.name = name
        self.__class__.instances.append(self)
    
    def propName(self):
        return self.name
    
    def base_url(self): 
        pass
    
    def sub_domain_url(self): 
        pass

    def html_xml_node(self): 
        pass

    def xpath_expression(self): 
        pass

    def test(self):
        print("The enrichment from AnotherSubclass")

    def base_test(self):
        super().base_test()

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())
