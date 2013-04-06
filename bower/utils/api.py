import json
import gzip
from StringIO import StringIO
import sublime

try:
  # ST3
  import urllib.request as req
except ImportError: 
  import urllib2 as req

try:
  # ST3
  from io import StringIO 
except ImportError:
  from StringIO import StringIO

class API():
  def get(self, endpoint, *args):
    host = "http://bower.herokuapp.com/"
    request = req.Request(host + endpoint)
    request.add_header('Accept-encoding', 'gzip')

    try:
      response = req.urlopen(request)
    except:
      sublime.error_message('Unable to connect to ' + host + endpoint + ". Check your internet connection.")

    if response.info().get('Content-Encoding') == 'gzip':
      buf = StringIO( response.read() )
      f = gzip.GzipFile(fileobj=buf)
      responseText = f.read()           
    else:
      responseText = response.read()

    try:
      return json.loads(responseText)
    except:
      sublime.error_message('Oh Snap! It looks like theres an error with the Bower API.')
  