import os, sys
try:
    __import__("green").menu()
except Exception as e:
    exit(str(e))
