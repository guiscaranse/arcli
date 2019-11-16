import os

from arcli.shared.db import SharedDB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.join(BASE_DIR, "..")
SHARED_DB = SharedDB(os.path.join(os.path.expanduser("~"), '.arcli.json'), True)
