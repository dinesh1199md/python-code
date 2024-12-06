from config_parser_module.config_reader import ConfigParserModule

config_parser = ConfigParserModule()

# Read YAML file 
config_dict = config_parser.read_yaml(r'C:\Users\dinesh.murugesan02\OneDrive - Infosys Limited\datascience-python\python-practicecode\functions-options\krishna-config\config.yaml')
print(config_dict)

config_parser.write_env("./config.env")
# # Read CFG or CONF file
# config_dict = config_parser.read_cfg('config.cfg')

