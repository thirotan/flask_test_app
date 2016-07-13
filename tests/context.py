import sys, os

basedir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, basedir + '/../')

from first_app import webapp
