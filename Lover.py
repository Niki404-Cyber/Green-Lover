import os, sys
try:
    __import__("AIM").menu()
except Exception as e:
    exit(str(e))
