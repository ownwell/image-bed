from PIL import ImageGrab, Image 
import time
import subprocess
import sys
import os


# father_path=os.path.abspath(os.path.dirname(os.path.abspath(__file__))+os.path.sep+".")
# print(father_path)

def father_path(path):

    father_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
    return father_path

 
imgUrl = ""

current_path = os.path.dirname(os.path.abspath(__file__))
script_path = father_path(current_path)

path = script_path

print("path = %s" % path)
def timestamp_to_date(time_stamp, format_string="%Y-%m-%d-%H-%M-%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date

def saveClipboardImg():
    im = ImageGrab.grabclipboard()



    if isinstance(im, Image.Image):
        global imgUrl

        print(im.format, im.size, im.mode)
        date = int(time.time())
        now = timestamp_to_date(date)
        filename =  str(now) + ".jpg"
        imgUrl = "https://raw.githubusercontent.com/ownwell/image-bed/master/img/"+filename
        print(imgUrl)
        im.save(path  +os.path.sep + "img"+os.path.sep +  filename, im.format)
        width, height = im.size
        pix = im.load()
    
    else:
        print("not image")
    pass

def pullToGithub():
    cmd = '''
    cd ''' + script_path + ''' ;git add .;git commit -m "blog_img";git push origin master
    '''
    subprocess.call(cmd, shell=True)


saveClipboardImg()
pullToGithub()
print("![](%s)"% imgUrl)