from com.thoughtworks.core import *

class Application:
    
    def __init__(self, scmReader=None):
        self.scmReader = scmReader
        self.map = {}
        self.id = -1
    
    def find(self, id):
        if id in self.map:
            return self.map[id]
        
    def projects(self):
        str = ""
        for p in self.map.values():
            str += serialize(p)
        return str
    
    def saveProject(self, projectString):
        p = deserialize(projectString)
        p.id = self.generateIdForProject()
        p.scmReader = self.scmReader
        p.fetchChangeSets()
        
        self.map[p.id] = p
        return p.id 
    
    def updateProject(self, projectString, id):
        project = deserialize(projectString)
        p = self.map[id]
        p.name = project.name
        p.developers = project.developers
        p.path = project.path
    
    def toCSV(self, id):
        project = self.find(id) 
        return project.toCSV()
    
    def generateIdForProject(self):
        id = -1
        for i in self.map:
            if id <= i: id = i
        return id + 1