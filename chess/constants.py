import os

CWD = os.path.dirname(__file__)
BIN = CWD + '/bin/'
CLASES = CWD + '/clases/'
ASSETS = CWD + '/assets/'
SAVES = CWD + '/saves/'
SRC = ASSETS + 'src/'

FULL_PATH = os.path.dirname(CWD)

with open(FULL_PATH + '/LICENSE', 'r') as L: LICENSE = L.read()
with open(FULL_PATH + '/README.md', 'r') as R: README = R.read()
