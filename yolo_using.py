import os
import subprocess
os.chdir('yolov7')
subprocess.run(['pip', 'install', '-qr', 'requirements.txt'])
import shutil
subprocess.run(['python', 'detect.py', '--source', 'test_images', '--weights', 'best4.4.pt'])
