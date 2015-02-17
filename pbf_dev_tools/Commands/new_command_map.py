from pbf.helpers.file_helper import IsDirectory
from pbf_dev_tools.templates import TemplatesRoot
from pbf.templates import template_manager

import os

class NewCommandMap:
    """ Command to create a new command map file """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createCommandMap(filepath)
        
    def createCommandMap(self, filepath):
        """ Create a Command Map """
        if IsDirectory(filepath):
            filepath = os.path.join(filepath, 'command_map.py')
        keywords = {}
        template_manager.CopyTemplate(filepath, "command_map.py", keywords, TemplatesRoot)