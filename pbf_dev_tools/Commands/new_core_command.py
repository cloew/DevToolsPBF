from pbf.Commands import command_manager
from pbf.Commands.PBF.new_command import NewCommand

import os

class NewCoreCommand:
    """ COmmand to create a new Command to include with the Core PBF installation """
    category = "new"
    command = "core-command"
    description = "Create a new PBF command to be stored with the core PBF installation"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filename', action='store', help='Filename of the new core PBF command to create')
    
    def run(self, arguments):
        """ Run the command """
        filename = arguments.filename
        print "Creating core command:", filename
        self.createCoreCommand(filename)
    
    def createCoreCommand(self, filename):
        """ Create the core command """
        pbfCommandsDirectory = os.path.join(os.path.dirname(__file__), '../')
        NewCommand().createNewCommand(os.path.join(pbfCommandsDirectory, filename))
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [command name]".format(category=self.category, command=self.command)
        print "Creates a new PBF command with the name given in the core PBF installation."
    
# command_manager.RegisterCommand(NewCoreCommand)