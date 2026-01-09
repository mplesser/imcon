"""
Starts the imcon application.
"""

import sys
import os

import IPython

from imcon.ipython_config import ipython_config


def main():
    """
    Starts imcon.
    Usage examples: imcon full_path_to_config_file
                    python -m imcon full_path_to_config_file
    """

    print("Welcome to imcon")

    # configure IPython
    c = ipython_config()

    # check for config file as first argument on command line
    if len(sys.argv) == 1:
        config_file = ""
        print("no configuration file specified")
    else:
        config_file = sys.argv[1]
        print("configuration file is", config_file)

        # add config_file folder to Python search path
        config_folder = os.path.dirname(config_file)
        config_file = os.path.basename(config_file)
        if config_file.endswith(".py"):
            config_file = config_file[:-3]
        sys.path.append(config_folder)

        # import config_file when IPython starts
        config_command = f"from {config_file} import *"
        c.InteractiveShellApp.exec_lines.append(config_command)

        # optimize for imcon instead of azcam
        _cmd = f"import imcon.optimize"
        c.InteractiveShellApp.exec_lines.append(_cmd)

        # import Tools to IPython CL
        config_command = f"from azcam.cli import *"
        c.InteractiveShellApp.exec_lines.append(config_command)

    # start IPython in interactive mode
    IPython.start_ipython([], config=c)

    print("Exited embedded IPython")


if __name__ == "__main__":
    imcon = main()
