# Mamoru Helper
This repository is for the helper tool used to translate the game. If you're looking for the English patch, click [here](http://www.romhacking.net/translations/5796/).  
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

## Text Editing
Editing the text can be done using MamoruTrans by DarthNemesis.

Run Mamoru Helper and extract `mamoru.nds`.  
Download [MamoruTrans 0.2.zip](https://code.google.com/archive/p/darthnemesis/downloads) and extract it to the `data\MamoruTrans` folder.  
Copy (don't cut) the `extract` folder created by running MamoruHelper, paste it into the `data\MamoruTrans` folder, and rename it `NDS_UNPACK`. You should now have two copies of the files extracted from the game, the original `data\extract` folder, and your copied `data\MamoruTrans\NDS_UNPACK` folder.  
Run MamoruTrans and click "Load All" to load the game files.  
Click "File" > "Export Text" to dump the script from the game files.  
Edit the .sjs files in the new `data\MamoruTrans\text\` folder in your editor of choice.  
Click "File" > "Import Text", then "File" > "Save All" to import the new script.

## Image Editing
Rename the out\_\* folders to work\_\* (out_IMG to work_IMG, etc).  
Edit the images in the work folder(s). The palette on the right should be followed but the repacker will try to approximate other colors to the closest one.  
If an image doesn't require repacking, it should be deleted from the work folder.  

## Repacking the Game
When setup correctly, running the Mamoru Helper repack command will repack both the text files in the MamoruTrans folder, and the images in the work_IMG folder, as well as applying bug fixes and feature improvements not possible by using MamoruTrans alone.
