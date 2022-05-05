import urllib
from urllib.request import urlopen

class InternetConnectionValidator:
    def __init__(self) -> None:
        pass
    
    def is_cnx_active(self,timeout=5):
        try:
            res = urlopen('https://www.google.com', timeout=timeout)
            return True
        except: 
            return False