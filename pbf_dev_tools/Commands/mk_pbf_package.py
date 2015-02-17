from pbf.Commands.PBF.new_pbf_properties import NewPbfProperties
from pbf.Commands.PBF.insert_pbf_package import InsertPbfPackage

from pbf.helpers.file_helper import CreateDirectoryIfItDoesNotExist

from pbf_dev_tools.Commands.mk_templates_dir import MakeTemplatesDirectory
from pbf_dev_tools.Commands.new_command_map import NewCommandMap
from pbf_python.Commands.mk_pydir import MakePyDir

from pbf.templates import template_manager
from pbf_dev_tools.templates import TemplatesRoot

import os

class MakePBFPackage:
    """ Command to make a new PBF Package """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('packagePath', action='store', help='Directory to create PBF Package')
        parser.add_argument('packageName', action='store', help='Name of the PBF Package')
    
    def run(self, arguments):
        """ Run the command """
        packagePath = arguments.packagePath
        packageName = arguments.packageName
        
        print "Making PBF Package at:", packagePath, "for package:", packageName
        self.createNewPackage(packagePath, packageName)
        
    def createNewPackage(self, packagePath, packageName):
        """ Create a new PBF Package """
        CreateDirectoryIfItDoesNotExist(packagePath)
        
        self.createPackageDirectories(packagePath, packageName)
        self.createPBFProperties(packagePath, packageName)
        self.prepareSetupFile(packagePath, packageName)
        
    def createPackageDirectories(self, packagePath, packageName):
        """ Create Package Directories """
        currentDirectory = packagePath
        pythonDirectoryMaker = MakePyDir()
        
        currentDirectory = os.path.join(currentDirectory, packageName)
        pythonDirectoryMaker.makePyDir(currentDirectory)
        NewCommandMap().createCommandMap(currentDirectory)
            
        pythonDirectoryMaker.makePyDir(os.path.join(currentDirectory, "Commands"))
        self.createTemplatesDirectory(currentDirectory)
        
    def createTemplatesDirectory(self, pbfPackageRoot):
        """ Creates the templates Directory in the directory given """
        templateDirectoryMaker = MakeTemplatesDirectory()
        templateDirectoryMaker.makeTemplatesDirectory(pbfPackageRoot)
        
    def createPBFProperties(self, packagePath, packageName):
        """ Creates the templates Directory in the directory given """
        NewPbfProperties().createPropertiesFile(packagePath)
        InsertPbfPackage().insertPBFPackage(os.path.join('.', packageName), packagePath)
            
    def prepareSetupFile(self, packagePath, packageName):
        """ Prepares the PBF Package Setup file """
        destination = os.path.join(packagePath, "setup.py")
        keywords = {"%PackagePath%":packageName,
                    "%PackageName%":packageName}
        template_manager.CopyTemplate(destination, "setup.py", keywords, templates_directory=TemplatesRoot)