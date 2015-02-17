from %PackageRoot%.templates import TemplatesRoot
from pbf.templates import template_manager

class %CommandClassName%:
    """ ADD DESCRIPTION HERE """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.create%CapitalCommandName%(filepath)
        
    def create%CapitalCommandName%(self, filepath):
        """ Create a %CapitalCommandName% """
        keywords = {}
        template_manager.CopyTemplate(filepath, """ TEMPLATE_FILENAME """, keywords, TemplatesRoot) # Add proper template file name here