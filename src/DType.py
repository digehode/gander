import os
class DType(object):
    def __init__(self, name):
        self.tests=[]
        self.name=name
    def addTest(self,test):
        self.tests.append(test)
    
class DTest(object):
    def __init__(self, name, requirements=[], priority=50, fn=lambda x: False):
        self.name=name
        self.requirements=requirements
        self.priority=priority
        self.fn=fn
        
class DData(object):
    def __init__(self):
        self.data=None
    def bit(self,n):
        return None
    def hbit(self,n):
        return None
    def checkReq(self,req):
        return False

class DDataFile(DData):
    def __init__(self,filename):
        self.data=open(filename)
    def checkReq(self,req):
        if req[0]=="bytes":

            if os.fstat(self.data.fileno()).st_size>=req[1][1]:
                return True
        return False
    def bit(self,n):
        self.data.seek(n)
        return self.data.read(1)
    def hbit(self,n):

        return hex(ord(self.bit(n)))[2:].zfill(2)
        
    
