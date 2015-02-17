from pbf.templates import template_manager
from pbf_dev_tools.templates import TemplatesRoot

import os

class MakeTemplatesDirectory:
    """ Command to make a PBF Templates Directory """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('directory', action='store', help='Directory to create PBF Template Directory in')
    
    def run(self, arguments):
        """ Run the command """
        directory = arguments.directory
        
        print "Creating templates directory in:", directory
        self.makeTemplatesDirectory(directory)
        
    def makeTemplatesDirectory(self, directory):
        """ Make the Template Directory in the directory specified """
        directory = os.path.join(directory, 'templates')
        os.mkdir(directory)
        
        initPath = os.path.join(directory, '__init__.py')
        template_manager.CopyTemplate(initPath, "template_init.py", templates_directory=TemplatesRoot)