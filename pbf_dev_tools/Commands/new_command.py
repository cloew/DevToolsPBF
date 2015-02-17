from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf_dev_tools.helpers.command_helper import GetCommandClassName, GetCommandCategoryAndCommand
from pbf_dev_tools.Commands.insert_command_config import InsertCommandConfig

from pbf.templates.template_loader import TemplateLoader
from pbf_dev_tools.templates import TemplatesRoot

class NewCommand:
    """ Creates a new PBF Command file """
    TEMPLATE_LOADER = TemplateLoader("command.py", TemplatesRoot)
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='The destination filename to create')
        parser.add_argument('-p', '--private', action='store_true', help='Specify that the command is private and should not be added to the Command Map')
    
    def run(self, arguments):
        """ Run the Command """
        filepath = arguments.destination
        print "Creating PBF Command:", GetPythonClassnameFromFilename(filepath), "at:", filepath
        self.createNewCommand(filepath, private=arguments.private)
        
    def createNewCommand(self, filepath, keywords=None, private=False):
        """ Create a new command at the filepath provided """
        if keywords is None:
            keywords = {}
        classname = GetCommandClassName(filepath)
        keywords["%CommandClassName%"] = classname
        
        if not private:
            InsertCommandConfig().insertCommandConfig(filepath)
        self.TEMPLATE_LOADER.copy(filepath, keywords=keywords)
        