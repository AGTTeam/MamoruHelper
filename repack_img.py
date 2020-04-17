import os
import game
from hacktools import common, nitro


def run():
    workfolder = "data/work_IMG/"
    infolder = "data/extract/data/"
    outfolder = "data/repack/data/"

    common.logMessage("Repacking IMG from", workfolder, "...")
    files = common.getFiles(infolder, [".NCGR", ".nbfs"])
    for file in common.showProgress(files):
        common.logDebug("Processing", file, "...")
        extension = os.path.splitext(file)[1]
        palettes, image, map, cell, width, height, mapfile, cellfile = game.readImage(infolder, file, extension)
        if image is None:
            continue
        pngfile = file.replace(extension, ".psd")
        if not os.path.isfile(workfolder + pngfile):
            pngfile = file.replace(extension, ".png")
            if not os.path.isfile(workfolder + pngfile):
                continue
        common.makeFolders(outfolder + os.path.dirname(file))
        common.copyFile(infolder + file, outfolder + file)
        if map is None and cell is None:
            nitro.writeNCGR(outfolder + file, image, workfolder + pngfile, palettes, width, height)
        elif cell is None:
            common.copyFile(infolder + mapfile, outfolder + mapfile)
            trasptile = "SN/CMN" in file
            nitro.writeMappedNSCR(outfolder + file, outfolder + mapfile, image, map, workfolder + pngfile, palettes, width, height, trasptile)
        else:
            common.copyFile(infolder + cellfile, outfolder + cellfile)
            nitro.writeNCER(outfolder + file, outfolder + cellfile, image, cell, workfolder + pngfile, palettes, width, height)
    common.logMessage("Done!")
