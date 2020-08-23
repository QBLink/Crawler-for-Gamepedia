import requests
from bs4 import BeautifulSoup
import os

#One example of the picture url to be downloaded:https://dragalialost.gamepedia.com/File:110064_01_r04_portrait.png
#https://dragalialost.gamepedia.com/File: + filename 

url = "https://dragalialost.gamepedia.com/index.php?title=Category:Character_Portrait_Images&filefrom=110064+01+r04+portrait.png#mw-category-media"
r = requests.get(url) #find the page of Category:Character_Portrait_Images

soup = BeautifulSoup(r.text, "html.parser")
imagelist = soup.find_all('div', attrs = {'class' : 'gallerytext'}) #find the filenames of all images

imagename = [] #make the list of filenames of images
for image in imagelist:
    a = image.a.text
    imagename.append(a)

imageurl_list = [] #use the filename to find the download url of image
for image in imagename:
    imageurl = "https://dragalialost.gamepedia.com/" +"File:" + image
    imageurl_list.append(imageurl)

i = 0
folder = "D:/ADV/Generator/Dataset_original/fgimage_dragalia/" #download pictures to this folder
for image in imageurl_list:
    req = requests.get(image)
    soup = BeautifulSoup(req.text, "html.parser")
    item = soup.find('img')

    if item:
        urls = item.get('srcset')
        urll = urls.split(',')[0]
        req = requests.get(urll)
        name = folder + imagename[i] + ".png"
        with open(name, 'wb') as file:  
            file.write(req.content)
            file.flush()
        file.close()
    i = i + 1
