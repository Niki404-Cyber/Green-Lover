import os, sys
try:
    __import__("green").approval()
except Exception as e:
    exit(str(e))
