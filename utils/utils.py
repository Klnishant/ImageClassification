import base64

def decodeImage(imgstring,filename):
    imagedata = base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imagedata)
        f.close()

def encodeImage(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return (base64.b64encode(f.read()))