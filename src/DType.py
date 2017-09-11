class DType(object):
    def __init__(self):
        self.tests=[]
    def addTest(self,test):
        self.tests.append(test)
    
class DTest(object):
    def __init__(self, name, requirements=[], priority=50):
        self.name=name
        self.requirements=requirements
        self.priority=priority
        
