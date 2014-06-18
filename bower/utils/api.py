import json
import gzip
import urllib.error
import sublime

try:
    # ST3
    import urllib.request as req
except ImportError:
    # ST2
    import urllib2 as req

try:
    # ST3
    from io import StringIO
except ImportError:
    # ST2
    from StringIO import StringIO


class API():
    def get(self, endpoint, host, *args):
        if not host:
            sublime.error_message('No registry URL specified')
            raise Exception('No registry URL specified')

        request = req.Request(host + '/' + endpoint)

        try:
            response = req.urlopen(request)
        except urllib.error.HTTPError:
            sublime.error_message('Unable to connect to ' + host + '/' + endpoint + ". Check your internet connection.")

        responseText = response.read().decode('utf-8', 'replace')

        try:
            return json.loads(responseText)
        except:
            sublime.error_message('Oh Snap! It looks like theres an error with the Bower API.')