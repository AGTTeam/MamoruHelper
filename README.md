# Mamoru Helper
This repository is for the tool used to translate the game. If you're looking for the English patch, click [here](http://www.romhacking.net/translations/5796/).  
## Setup
Install [Python 3](https://www.python.org/downloads/).  
Install [ImageMagick](https://imagemagick.org/script/download.php). For Windows, check "Add application directory to your system path" while installing.  
Download this repository by downloading and extracting it, or cloning it.  
Copy the original Japanese rom into the same folder and rename it as `mamoru.nds`.  
Run `run_windows.bat` (for Windows) or `run_bash` (for OSX/Linux) to run the tool.  
## Run from command line
This is not recommended if you're not familiar with Python and the command line.  
After following the Setup section, run `pipenv sync` to install dependencies.  
Run `pipenv run python tool.py extract` to extract everything, and `pipenv run python tool.py repack` to repack.  
You can use switches like `pipenv run python tool.py repack --bin` to only repack certain parts to speed up the process.  
