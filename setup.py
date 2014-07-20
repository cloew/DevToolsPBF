from distutils.core import setup

setup(name='pbf_dev_tools',
      version='.1',
      description="Programmer's Best Friend Utility Extension for pbf_dev_tools",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_dev_tools', 'pbf_dev_tools.Commands', 'pbf_dev_tools.templates'],
      package_data = {'pbf_dev_tools.templates':['*']},
     )