from pbf.templates.template_loader import TemplateLoader
from pbf_dev_tools.templates import TemplatesRoot

class NewCommandMap:
    """ Command to create a new command map file """
    TEMPLATE_LOADER = TemplateLoader("command_map.py", TemplatesRoot, defaultFilename="command_map.py")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createCommandMap(filepath)
        
    def createCommandMap(self, filepath):
        """ Create a Command Map """
        self.TEMPLATE_LOADER.copy(filepath)