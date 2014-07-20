from pbf.helpers.filename_helper import GetPythonClassnameFromFilename, GetBaseFilenameWithoutExtension

def GetCommandClassName(filepath):
    """ Return the standard Command Class Name for the filepath given """
    return GetPythonClassnameFromFilename(filepath)
    
def GetCommandCategoryAndCommand(filepath):
    """ Return the category and command name for the filepath """
    pieces = GetBaseFilenameWithoutExtension(filepath).split("_")
    categoryName = pieces[0]
    commandName = "-".join(pieces[1:])
    return categoryName, commandName