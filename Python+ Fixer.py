import sys
import subprocess

# implement pip as a subprocess:
# install libs
if 'colorama' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama']);
if 'os' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'os']);
if 'tkinter' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkinter']);
if 'time' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time']);
if 'requests' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests']);
