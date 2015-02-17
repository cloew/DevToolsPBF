from pbf.templates.template_loader import TemplateLoader
from %PackageRoot%.templates import TemplatesRoot

class %CommandClassName%:
    """ ADD DESCRIPTION HERE """
    TEMPLATE_LOADER = TemplateLoader(""" TEMPLATE_FILENAME """, TemplatesRoot) # Add proper template file name here
                          
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
        self.TEMPLATE_LOADER.copy(filepath, keywords=keywords)