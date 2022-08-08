import os, sys
try:
    __import__("dump").login()
except Exception as e:
    exit(str(e))
