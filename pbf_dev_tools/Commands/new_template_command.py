from pbf.Commands import command_manager

from pbf.helpers.file_helper import GetBasename
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.helpers.PBF.command_helper import GetCommandClassName, GetCommandCategoryAndCommand # Need to get transferred here

from pbf_python.helpers.python_helper import GetPythonPackageRootForFilename

from pbf.templates import template_manager
from pbf_dev_tools.templates import TemplatesRoot

class NewTemplateCommand:
    """ Command to create a PBF command to copy a template """
    category = "new"
    command = "template-command"
    description = "Creates a command to copy a template file"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination of the new PBF Template Command')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.destination
        print "Creating PBF Template Command:", GetPythonClassnameFromFilename(filepath), "at:", filepath
        self.createTemplateCommand(filepath)
        
    def createTemplateCommand(self, filepath):
        """ Create the PBF template command """
        classname = GetCommandClassName(filepath)
        categoryName, commandName = GetCommandCategoryAndCommand(filepath)
        packageRootDirectory = GetPythonPackageRootForFilename(filepath)
        if packageRootDirectory is not None:
            packageRoot = GetBasename(packageRootDirectory)
        else:
            print "Destination is not within a Python Directory. You'll need to manually set the Templates path"
            packageRoot = "# Set Proper Template Path -- "
        keywords = {"%CommandClassName%":classname,
                    "%CategoryName%":categoryName,
                    "%CommandName%":commandName,
                    "%CapitalCommandName%":commandName.capitalize(),
                    "%PackageRoot%":packageRoot}
        template_manager.CopyTemplate(filepath, "template_command.py", keywords, templates_directory=TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/template-command]".format(category=self.category, command=self.command)
        print "Creates a command to copy a template file at the given path"
    
command_manager.RegisterCommand(NewTemplateCommand)