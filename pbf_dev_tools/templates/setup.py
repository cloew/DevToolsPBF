from distutils.core import setup

setup(name='%PackagePath%',
      version='.1',
      description="Programmer's Best Friend Utility Extension for %PackageName%",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['%PackagePath%', '%PackagePath%.Commands', '%PackagePath%.templates'],
      #package_data = {'%PackagePath%.templates':[]}, # Add template files
     )