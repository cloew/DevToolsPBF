from pbf.Commands import command_manager
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.helpers.PBF.command_helper import GetCommandClassName, GetCommandCategoryAndCommand


from pbf.templates import template_manager
from pbf_dev_tools.templates import TemplatesRoot

import os

class NewCommand:
    """ Creates a new PBF Command file """
    category = "new"
    command = "command"
    description = "Create a new PBF command file"
    
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
    
    def help(self):
        """ Print the Usage of the New Main Command """
        print "Usage: pbf {category} {command} [path/to/command]".format(category=self.category, command=self.command)
        print "\tWill create a PBF Command at the path given"
    
command_manager.RegisterCommand(NewCommand)