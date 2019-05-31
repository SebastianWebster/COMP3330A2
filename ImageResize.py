from PIL import Image
import os
import glob

def shrink_all(xdim,ydim,path):
    for img in glob.glob(path+"/*.JPG"):
        file,ext = os.path.splitext(img)
        im = Image.open(img)
        im = im.resize([xdim,ydim])
        im.show()
        im.save(file + "_mini.JPG","JPEG")



def main():
    path = os.path.join(os.getcwd(),'Test')
    shrink_all(64,64,path)

main()