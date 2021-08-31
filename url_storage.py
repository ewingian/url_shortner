
import zlib
import re
from urllib.parse import urlparse


class UrlUtilites:
    ''' instantiate a url data store
    and provide methods for retriving, shortening,
    and storing '''

    def __init__(self):
        self.url_storage = {}

    def store_url(self, id, short_url, normal_url):
        ''' Store a url in memory and
        key it to an id '''
        if id in self.url_storage:
            self.url_storage[id] = {
                'short_url': short_url,
                'normal_url': normal_url,
            }
        else:
            self.url_storage[id] = ''
            self.url_storage[id] = {
                'short_url': short_url,
                'normal_url': normal_url,
            }
        print(self.url_storage)

    def retrieve_normal_url(self, id):
        ''' Given an id from a shortened url retrieve the
        full length counterpart
        Inputs:
        -------
        id: the numerical id that is the shortened version of a url

        Outputs:
        --------
        url: returns the original url
        '''
        print(id)
        print(self.url_storage)
        print(repr(id))
        print(repr(self.url_storage))
        if self.url_storage.get(id) is not None:
            return self.url_storage[id]['normal_url'], 200
        # if id in self.url_storage.keys():
        #     return self.url_storage[id]['normal_url'], 200
        else:
            return f"No id of {id} found", 404

    def shorten_url(self, url):
        ''' take in url, strip off first part of url for later,
        check for certain types of urls, and reduce url '''
        # not base64 but that could be done later
        # for now just trying to generate an ID
        parsed_url = urlparse(url)
        id = zlib.crc32(url.encode())
        shortened_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{id}"
        return {'id': id,
                'shortened_url': shortened_url,
                'normal_url': url}
