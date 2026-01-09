"""
imcon example start file
"""

import subprocess

OPTIONS = "-system test"
CMD = f"ipython --profile imcon -i -m imcon -- {OPTIONS}"

p = subprocess.Popen(
    CMD,
    creationflags=subprocess.CREATE_NEW_CONSOLE,
)
