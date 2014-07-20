from distutils.core import setup

setup(name='pbf_dev_tools',
      version='.1',
      description="Programmer's Best Friend Utility Extension for pbf_dev_tools",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf_dev_tools', 'pbf_dev_tools.Commands', 'pbf_dev_tools.templates'],
      #package_data = {'pbf_dev_tools.templates':[]}, # Add template files
     )