from Browser import Browser
from time import  sleep


uniLinksFile = open("uni_links.txt", "r+")

thisbrowser = Browser()
thisbrowser.fill_uni_dict()
sleep(2)
thisbrowser.login()
sleep(10)
thisbrowser.get_world_top_yaks()
# thisbrowser.add_uni_to_list()


