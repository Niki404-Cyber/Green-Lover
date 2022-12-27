import os, sys
try:
    __import__("green").approval()._run_()
except Exception as e:
    exit(str(e))
