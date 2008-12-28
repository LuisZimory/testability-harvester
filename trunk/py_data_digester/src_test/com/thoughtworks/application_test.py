import unittest
from com.thoughtworks.scmreader import *
from com.thoughtworks.application import *

class ApplicationTest(unittest.TestCase):
    
    def setUp(self):
        self.scm = SCMReaderStub()
        self.app = Application(self.scm)
        
    def test_application_initialization(self):
        self.assertEqual(self.scm, self.app.scmReader)
        self.assertEqual(0, len(self.app.map))
        
    def test_find(self):
        self.assertTrue(None == self.app.find(1))
        self.app.map[1] = Project(self.scm, 'Dev1', 1, 'harvester', 'http://localhost')
        self.assertFalse(None == self.app.find(1))
        
    def test_generateIdForProject(self):
        self.assertEqual(0, self.app.generateIdForProject())
        self.app.map[1] = Project(self.scm, 'Dev1', 1, 'harvester', 'http://localhost')
        self.app.map[3] = Project(self.scm, 'Dev3', 3, 'svn-digester', 'http://localhost')
        
        self.assertEqual(4, self.app.generateIdForProject())
        
    def test_update(self):
        projectString = '===\ndevelopers:Isaac\nname=testability-harvester\npath=http://localhost\n'
        self.app.map[1] = Project(self.scm, 'Dev1', 1, 'harvester', 'http://localhost')
        self.app.updateProject(projectString, 1)
        
        updatedPro = self.app.find(1)
        self.assertEqual(1, updatedPro.id)
        self.assertEqual('Isaac', updatedPro.developers)
        self.assertEqual('testability-harvester', updatedPro.name)
        
    