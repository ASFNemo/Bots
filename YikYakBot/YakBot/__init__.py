from Browser import Browser
from time import  sleep


uniLinksFile = open("uni_links.txt", "r+")

thisbrowser = Browser()
sleep(2)
thisbrowser.login()
sleep(10)
thisbrowser.get_world_top_yaks()


