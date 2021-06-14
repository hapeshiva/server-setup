@echo off
python -m pip install --upgrade pip
pip3 install psutil
pip3 install requests
echo "Warning! if modules cannot be found please check that you do not have multiple python versions!"
python setup.py
pause
