from PIL import ImageGrab, Image 
import time
import subprocess
import sys
import os

print(os.chdir(sys.path[0]))

 
imgUrl = ""
path = "/Users/lixingyun/work/private/image/"
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
        imgUrl = "https://raw.githubusercontent.com/ownwell/image-bed/master/"+filename
        print(imgUrl)
        im.save(path +  filename, im.format)
        width, height = im.size
        pix = im.load()
    
    else:
        print("not image")
    pass

def pullToGithub():
    cmd = '''
    cd ''' + path + ''' ;git add .;git commit -m "blog_img";git push origin master
    '''
    subprocess.call(cmd, shell=True)

      

saveClipboardImg()
pullToGithub()
print("![](%s)"% imgUrl)