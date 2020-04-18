import os
import click
import game
from hacktools import common, nds, nitro

version = "0.3.2"
romfile = "data/mamoru.nds"
rompatch = "data/mamoru_patched.nds"
infolder = "data/extract/"
replacefolder = "data/replace/"
outfolder = "data/repack/"
mtransbin = "data/MamoruTrans/NDS_UNPACK/arm9.bin"
mtransbinout = "data/repack/arm9.bin"
mtransparm = "data/MamoruTrans/NDS_UNPACK/data/Proj60.dat"
mtransparmout = "data/repack/data/Proj60.dat"
bannerfile = "data/repack/banner.bin"
patchfile = "data/patch.xdelta"


@common.cli.command()
@click.option("--rom", is_flag=True, default=False)
@click.option("--img", is_flag=True, default=False)
def extract(rom, img):
    all = not rom and not img
    if all or rom:
        nds.extractRom(romfile, infolder, outfolder)
    if all or img:
        nitro.extractIMG("data/extract/data/", "data/out_IMG/", [".NCGR", ".nbfs"], game.readImage)


@common.cli.command()
@click.option("--no-rom", is_flag=True, default=False)
@click.option("--mtrans", is_flag=True, default=False)
@click.option("--img", is_flag=True, default=False)
def repack(no_rom, mtrans, img):
    all = not mtrans and not img
    if all or mtrans:
        common.copyFile(mtransbin, mtransbinout)
        common.copyFile(mtransparm, mtransparmout)
        fontfiles = []
        fontfile = "data/replace/data/FONT/LC08.NFTR"
        fontfiles.append(fontfile if os.path.isfile(fontfile) else fontfile.replace("replace/", "extract/"))
        fontfile = "data/replace/data/FONT/LC10.NFTR"
        fontfiles.append(fontfile if os.path.isfile(fontfile) else fontfile.replace("replace/", "extract/"))
        nitro.extractFontData(fontfiles, "data/font_data.bin")
        common.armipsPatch("bin_patch.asm")
    if all or img:
        nitro.repackIMG("data/work_IMG/", "data/extract/data/", "data/repack/data/", [".NCGR", ".nbfs"], game.readImage, game.writeImage)
    if not no_rom:
        if os.path.isdir(replacefolder):
            common.mergeFolder(replacefolder, outfolder)
        nds.editBannerTitle(bannerfile, "I will protect you.\nIDEA FACTORY")
        nds.repackRom(romfile, rompatch, outfolder, patchfile)


if __name__ == "__main__":
    click.echo("MamoruHelper version " + version)
    if not os.path.isdir("data"):
        common.logError("data folder not found.")
        quit()
    common.cli()
