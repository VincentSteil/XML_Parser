# --------------------
# RunXML.py
# Lab 2
# Mateusz Dubaniowski
# Vincent Steil
# --------------------

"""
To document the program
% pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from XML import XML_parser

# ----
# main
# ----

XML_parser(sys.stdin, sys.stdout)
