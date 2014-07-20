from pbf.Commands import command_manager

class %CommandClassName%:
    """ ADD DESCRIPTION HERE """
    category = "%CategoryName%"
    command = "%CommandName%"
    description = "" # ADD DESCRIPTION HERE
                          
    def addArguments(self, parser): # ADD ARGUMENTS
        """ Add arguments to the parser """
        pass # No Arguments
        # Sample Argument: parser.add_argument('filename', action='store', help='Filename to open')
    
    def run(self, arguments):
        """ Run the command """
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "" # ADD DETAILED DESCRIPTION 
    
command_manager.RegisterCommand(%CommandClassName%)