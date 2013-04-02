import urllib2
import json
import gzip
from StringIO import StringIO
import sublime

class API():
  def get(self, endpoint, *args):
    host = "http://bower.herokuapp.com/"
    request = urllib2.Request(host + endpoint)
    request.add_header('Accept-encoding', 'gzip')

    try:
      response = urllib2.urlopen(request)
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
  