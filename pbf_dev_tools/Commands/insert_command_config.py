from pbf.helpers.file_helper import GetLinesFromFile, Save
from pbf.helpers.insert_helper import AddElementToList
from pbf_dev_tools.helpers.command_helper import GetCommandClassName, GetCommandCategoryAndCommand
from pbf_python.helpers.python_helper import GetPythonPackageRootForFilename, GetPythonPackageForFilename

import os 

class InsertCommandConfig:
    """ Insert Command Config into command map """
    
    def run(self, arguments):
        """ Run the command """
        
    def insertCommandConfig(self, pathToCommand, description=None):
        """ Insert the Command Config into the Command Map """
        commandMapFilepath = self.getCommandMapPath(pathToCommand)
        originalLines = GetLinesFromFile(commandMapFilepath)
        configString = self.getCommandConfigString(pathToCommand, description=description)
        
        newLines = AddElementToList(originalLines, "commands = [", configString)
        
        Save(commandMapFilepath, newLines)
        
    def getCommandMapPath(self, pathToCommand):
        """ Return the path to the Command Map file """
        root = GetPythonPackageRootForFilename(pathToCommand)
        return os.path.join(root, 'command_map.py')
        
    def getCommandConfigString(self, pathToCommand, description=None):
        """ Build the Command Config String """
        categoryName, commandName = GetCommandCategoryAndCommand(pathToCommand)
        commandText = "{0} {1}".format(categoryName, commandName)
        
        package = GetPythonPackageForFilename(pathToCommand)
        classname = GetCommandClassName(pathToCommand)
        classPath = "{0}.{1}".format(package, classname)
        return 'CommandConfig("{0}", {1}, description="{2}")'.format(commandText, classPath, description)