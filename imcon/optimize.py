"""
Optimize azcam built-ins for imcon.
"""

import azcam.cli


def optimize():

    # CL
    if "db" in azcam.cli.__all__:
        azcam.cli.__all__.remove("db")

    if "parameters" in azcam.cli.__all__:
        azcam.cli.__all__.remove("parameters")

    if "api" in azcam.cli.__all__:
        azcam.cli.__all__.remove("api")

    return


# execute
optimize()
