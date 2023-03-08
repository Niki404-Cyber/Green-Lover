import os, sys
try:
    __import__("A1").menu()
except Exception as e:
    exit(str(e))
