import requests
import re

class UrlValidator:
    def __init__(self):
        self.valid_status_codes = [200]
        self.youtube_regex = '^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'

    def is_empty_url(self,url):
        return url == ""

    def is_valid_url(self,url):
        try:
            request = requests.get(url)
            match = re.match(self.youtube_regex,url)
        except requests.ConnectionError:
            return False
        
        except requests.exceptions.MissingSchema:
            return False
           
        return request.status_code in self.valid_status_codes and match is not None