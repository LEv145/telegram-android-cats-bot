import subprocess
from sys import argv


subprocess.run(f"mkinit {argv[1]} -w --black --nomods --relative --recursive".split())
