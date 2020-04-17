import os
from hacktools import nitro


def readImage(infolder, file, extension):
    cell = None
    if extension == ".NBFC":
        palettefile = file.replace(extension, ".NBFP")
        mapfile = file.replace(extension, ".NBFS")
        cellfile = ""
    elif extension == ".NTFT":
        palettefile = file.replace(extension, ".NTFP")
        mapfile = ""
        cellfile = ""
        map = None
    elif extension == ".NCGR":
        palettefile = file.replace(extension, ".NCLR")
        if not os.path.isfile(infolder + palettefile) and "OBJACT_" in palettefile:
            palettefile = "SN/ACT/OBJACT_BTM.NCLR"
        mapfile = file.replace(extension, ".NSCR")
        cellfile = file.replace(extension, ".NCER")
    # Read the image
    if extension == ".NBFC":
        palettes, image, map = nitro.readNitroGraphicNBFC(infolder + palettefile, infolder + file, infolder + mapfile)
        width = image.width
        height = image.height
    elif extension == ".NTFT":
        palettes, image = nitro.readNitroGraphicNTFT(infolder + palettefile, infolder + file)
        width = image.width
        height = image.height
    elif extension == ".NCGR":
        palettes, image, map, cell, width, height = nitro.readNitroGraphic(infolder + palettefile, infolder + file, infolder + mapfile, infolder + cellfile)
    return palettes, image, map, cell, width, height, mapfile, cellfile
