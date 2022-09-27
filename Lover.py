import os, sys
try:os.system('git pull')
except:pass
try:os.system('touch .prox.txt')
except:pass
try:
    __import__("full").sex_but_oky()
except Exception as e:
    exit(str(e))
