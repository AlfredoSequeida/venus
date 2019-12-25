import os

__version__ = '1.0.2'
__config__ = '[SETTINGS]\nSEARCH_TERMS =\nOUTPUT_PATH =\nWAIT_TIME =' 

dir_path_to_conf = os.path.join(os.path.expanduser('~'), '.config/venus')

if 'XDG_CONFIG_HOME' in os.environ:
    dir_path_to_conf = os.environ['XDG_CONFIG_HOME']

#setting up config file with setting options
file_path_to_conf = os.path.join(dir_path_to_conf, 'config')

if not os.path.exists(dir_path_to_conf):
    os.makedirs(dir_path_to_conf)

if not os.path.exists(file_path_to_conf):
    with open(file_path_to_conf, 'w') as f:
        f.write(__config__)
