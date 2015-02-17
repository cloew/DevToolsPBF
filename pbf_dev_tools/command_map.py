from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig('mk pbf-package', 'pbf_dev_tools.Commands.mk_pbf_package.MakePBFPackage', description="Make a PBF Package directory structure")]

RegisterCommands(commands)