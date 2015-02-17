from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig('mk pbf-package', 'pbf_dev_tools.Commands.mk_pbf_package.MakePBFPackage', description="Make a PBF Package directory structure"),
            CommandConfig('mk templates-dir', 'pbf_dev_tools.Commands.mk_templates_dir.MakeTemplatesDirectory', description="Create a PBF Templates Directory"),
            CommandConfig('new command', 'pbf_dev_tools.Commands.new_command.NewCommand', description="Create a new PBF command file"),
            CommandConfig('new template-command', 'pbf_dev_tools.Commands.new_template_command.NewTemplateCommand', description="Creates a command to copy a template file")]

RegisterCommands(commands)