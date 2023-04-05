import requests
import time
from sports import get_sports
from site_2 import get_matches


for i in get_sports():
    print(i,'====',get_matches(i))
    time.sleep(0.25)
