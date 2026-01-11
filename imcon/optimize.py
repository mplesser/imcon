"""
Optimize azcam built-ins for imcon.
Everything here is imported to the imcon CLI.
"""

import azcam

# set imports
tools = azcam.db.tools
pars = azcam.db.parameters
api = azcam.db.api

__all__ = ["azcam", "tools", "pars", "api"]
