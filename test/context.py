# Add the parent directory to the sys.path variable so that parent/sibling packages can be
# imported
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

