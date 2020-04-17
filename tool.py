import os
import click
from hacktools import common, nds

version = "0.3.0"
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
        import extract_img
        extract_img.run()


@common.cli.command()
@click.option("--no-rom", is_flag=True, default=False)
@click.option("--mtrans", is_flag=True, default=False)
@click.option("--img", is_flag=True, default=False)
def repack(no_rom, mtrans, img):
    all = not mtrans and not img
    if all or mtrans:
        common.copyFile(mtransbin, mtransbinout)
        common.copyFile(mtransparm, mtransparmout)
    if all or img:
        import repack_img
        repack_img.run()
    if not no_rom:
        if os.path.isdir(replacefolder):
            common.mergeFolder(replacefolder, outfolder)
        common.armipsPatch("bin_patch.asm")
        nds.editBannerTitle(bannerfile, "I will protect you.\nIDEA FACTORY")
        nds.repackRom(romfile, rompatch, outfolder, patchfile)


if __name__ == "__main__":
    click.echo("MamoruHelper version " + version)
    if not os.path.isdir("data"):
        common.logError("data folder not found.")
        quit()
    common.cli()
