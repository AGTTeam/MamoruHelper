import os
import game
from hacktools import common, nitro


def run():
    infolder = "data/extract/data/"
    outfolder = "data/out_IMG/"
    common.makeFolder(outfolder)

    common.logMessage("Extracting IMG to", outfolder, "...")
    files = common.getFiles(infolder, [".NCGR", ".NBFC", ".NTFT"])
    for file in common.showProgress(files):
        common.logDebug("Processing", file, "...")
        extension = os.path.splitext(file)[1]
        palettes, image, map, cell, width, height, mapfile, cellfile = game.readImage(infolder, file, extension)
        if image is None:
            continue
        # Export img
        common.makeFolders(outfolder + os.path.dirname(file))
        outfile = outfolder + file.replace(extension, ".png")
        if cell is not None:
            nitro.drawNCER(outfile, cell, image, palettes, True, True)
        else:
            nitro.drawNCGR(outfile, map, image, palettes, width, height)
    common.logMessage("Done! Extracted", len(files), "files")
