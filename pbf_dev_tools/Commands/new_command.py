from pbf.helpers.filename_helper import GetPythonClassnameFromFilename

from pbf_dev_tools.helpers.command_helper import GetCommandClassName, GetCommandCategoryAndCommand

from pbf.templates import template_manager
from pbf_dev_tools.templates import TemplatesRoot

import os

class NewCommand:
    """ Creates a new PBF Command file """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='The destination filename to create')
    
    def run(self, arguments):
        """ Run the Command """
        filepath = arguments.destination
        print "Creating PBF Command:", GetPythonClassnameFromFilename(filepath), "at:", filepath
        self.createNewCommand(filepath)
        
    def createNewCommand(self, filepath):
        """ Create a new command at the filepath provided """
        classname = GetCommandClassName(filepath)
        categoryName, commandName = GetCommandCategoryAndCommand(filepath)
        keywords = {"%CommandClassName%":classname,
                    "%CategoryName%":categoryName,
                    "%CommandName%":commandName}
        template_manager.CopyTemplate(filepath, "command.py", keywords, templates_directory=TemplatesRoot)