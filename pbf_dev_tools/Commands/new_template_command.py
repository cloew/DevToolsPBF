from pbf.helpers.file_helper import GetBasename

from pbf_dev_tools.helpers.command_helper import GetCommandCategoryAndCommand
from pbf_python.helpers.python_helper import GetPythonPackageRootForFilename

from pbf_dev_tools.Commands.new_command import NewCommand

from pbf.templates.template_loader import TemplateLoader
from pbf_dev_tools.templates import TemplatesRoot

class NewTemplateCommand(NewCommand):
    """ Command to create a PBF command to copy a template """
    TEMPLATE_LOADER = TemplateLoader("template_command.py", TemplatesRoot)
        
    def createNewCommand(self, filepath, private=False):
        """ Create the PBF template command """
        categoryName, commandName = GetCommandCategoryAndCommand(filepath)
        packageRootDirectory = GetPythonPackageRootForFilename(filepath)
        if packageRootDirectory is not None:
            packageRoot = GetBasename(packageRootDirectory)
            
        keywords = {"%CapitalCommandName%":commandName.capitalize(),
                    "%PackageRoot%":packageRoot}
                    
        NewCommand.createNewCommand(self, filepath, keywords=keywords, private=private)