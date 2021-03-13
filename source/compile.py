import os
import sys

dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)

os.system("cxfreeze -c time_reporting.py")
os.rename(os.path.join(dir, "dist"), os.path.join(dir, "..", "..", "time_reportingApp"))