#! /usr/bin/env python
import cgi, json, xmltodict
from collections import namedtuple

print "Content-Type: text/html"

import urllib2

def get_unread_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user=user,
        passwd=passwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen('https://mail.google.com/mail/feed/atom')
    return xmltodict.parse(feed.read())

form = cgi.FieldStorage()

emails = get_unread_msgs(form["username"].value, form["password"].value)

max = 50

if len(emails["feed"]["entry"]) > max:
	emails = emails["feed"]["entry"][0:max]
else:
	emails = emails["feed"]["entry"]

print ""
print json.dumps(emails)