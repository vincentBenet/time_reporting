import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cxfreeze -c time_reporting.py")