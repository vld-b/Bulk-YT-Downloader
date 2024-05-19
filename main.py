import pytube
import requests
import os

txtfile = open(input("Eingabe der txt datei: "), "r")

vids = txtfile.readlines()

for vid in vids:
    src = pytube.YouTube(vid)
    src.streams.get_highest_resolution().download(output_path="./"+src.title)
    print("Video: "+src.title+" heruntergeladen")
    with open(os.path.join(src.title, src.title+".png"), "a+b") as f:
        f.write(requests.get(src.thumbnail_url, stream=True).content)
        f.close()
    print("Thumbnail: "+src.title+" heruntergeladen")

txtfile.close()