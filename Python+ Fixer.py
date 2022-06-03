import sys
import subprocess

# implement pip as a subprocess:
# install libs
if 'py-console' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'py-console']);
if 'os' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'os']);
if 'tkinter' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkinter']);
if 'time' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time']);
if 'requests' not in sys.modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests']);
