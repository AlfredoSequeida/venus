import os

__version__ = "0.1.1"

dir_path_to_conf = os.path.join(os.path.expanduser('~'), '.config/venus')

if 'XDG_CONFIG_HOME' in os.environ:
    dir_path_to_conf = os.environ['XDG_CONFIG_HOME']

file_path_to_conf = os.path.join(dir_path_to_conf, 'config')
text = """[SETTINGS]
SEARCH_TERMS =
"""

if not os.path.exists(dir_path_to_conf):
    os.makedirs(dir_path_to_conf)

if not os.path.exists(file_path_to_conf):
    with open(file_path_to_conf, 'w') as f:
        f.write(text)
