from PIL import Image
import os
import glob

def shrink_all(xdim,ydim,path):
    for img in glob.glob(path+"/*.JPG"):
        file,ext = os.path.splitext(img)
        im = Image.open(img)
        im = crop_to_square(im)
        im.load()
        im = im.resize([xdim,ydim])
        im.show()
        im.save(file + "_mini.JPG","JPEG")

#    0,0__________
#       |        |
#       |  img   |
#       |________|
#                  maxx,maxy
#Crops the images square so they can be refered to in base2
def crop_to_square(im):
    #If width is greater than height we want to horizontally crop
    if(im.width!=im.height):
        if(im.width > im.height):
            offset = (im.width - im.height)/2
            return im.crop((offset,0,im.width-offset,im.height))
        else:
            offset = (im.height - im.width)/2
            return im.crop((0,offset,im.width,im.height-offset))
    else:
        print("Image xy already sqr")
        return im

def main():
    path = os.path.join(os.getcwd(),'Test')
    shrink_all(64,64,path)

main()