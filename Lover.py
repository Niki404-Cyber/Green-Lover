import os, sys
try:
    __import__("green").app_()
except Exception as e:
    exit(str(e))
