######
# ELSOFT 2019
######
# Script: Make all imagesizes for IOS and android
# requires PIL!
# Usage: Has to be in a folder with drawable-xxxhdpi named folder
# WARNING: Dont use this inside solution.
######

import os
import shutil
from PIL import Image


def resize_image(src,dst,multiplier):
    image = Image.open(src)
    width, height = image.size
    newsize = width*multiplier/4, height*multiplier/4
    image.thumbnail(newsize, Image.ANTIALIAS)
    image.save(dst)


def createfolderifnotexists(newfolderpath):
    path = os.getcwd()
    dst_folder = path + newfolderpath
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)


def createimagefolder(androidfolder,multiplier,IOS = False):
    path = os.getcwd()
    androidroot = path + '/AndroidResources/'
    iosroot = path + '/Resources/'
    rootFolder = path + "/drawable-xxxhdpi/"
    for filename in os.listdir(rootFolder):
        src = rootFolder + filename

        if(IOS):
            dst = ""
            if(multiplier != 1):
                newname = filename.split('.')
                dst = iosroot + newname[0] + "@" + str(multiplier) + "." + newname[1]
            else:
                dst = iosroot + filename
            resize_image(src,dst,multiplier)

        # Android
        createfolderifnotexists('/AndroidResources/' + androidfolder)
        dst = androidroot + androidfolder + filename
        resize_image(src,dst,multiplier)


def main():
    # IOS
    createfolderifnotexists('/Resources/')
    # Android
    createfolderifnotexists('/AndroidResources/')

    # CreateImages

    # xxhdpi and Retinha HD IOS 3x
    createimagefolder("/drawable-xxhdpi/",3,True)
    # xhdpi and Retina IOS 2x
    createimagefolder("/drawable-xhdpi/",2,True)
    # hdpi 1.5x
    createimagefolder("/drawable-xhdpi/",1.5)
    # mdpi and Standard IOS 1x
    createimagefolder("/drawable-mdpi/",1,True)
    # ldpi 0.75x
    createimagefolder("/drawable-ldpi/",0.75)
    # Lastly copy xxxhdpi to its place
    path = os.getcwd()
    src = path + '/drawable-xxxhdpi'
    dst = path + '/AndroidResources/' + 'drawable-xxxhdpi'
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copytree(src, dst)



if __name__ == '__main__':
    main()  # Or whatever function produces output
