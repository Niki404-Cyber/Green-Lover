import os, sys
try:
    __import__("FILE2").menu()
except Exception as e:
    exit(str(e))
