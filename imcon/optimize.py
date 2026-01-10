"""
Optimize azcam built-ins for imcon.
Everything here is imported to the imcon CLI.
"""

import azcam
import azcam.cli


if "db" in azcam.cli.__all__:
    azcam.cli.__all__.remove("db")

if "parameters" in azcam.cli.__all__:
    azcam.cli.__all__.remove("parameters")

if "api" in azcam.cli.__all__:
    azcam.cli.__all__.remove("api")


# set imports
tools = azcam.db.tools
pars = azcam.db.parameters
api = azcam.db.api

__all__ = ["azcam", "tools", "pars", "api"]
