import hashlib
import binascii
import sys,os
import time
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
from evernote.api.client import EvernoteClient
dev_token = "S=s345:U=39a79d5:E=14b41f1d370:C=143ea40a774:P=1cd:A=en-devtoken:V=2:H=db1266a393bb7007ee80ec1c27e5c7ec"
client = EvernoteClient(token=dev_token,sandbox=False)
userStore = client.get_user_store()
noteStore = client.get_note_store()
#user = userStore.getUser()
#print user.username
#noteStore = client.get_note_store()
#noteStore = client.get_note_store()
#note = Types.Note()
for filer in os.listdir("/Volumes/VOLUME1/DCIM/100MEDIA"):
	print filer
	note = Types.Note()
	note.title = str(time.ctime(os.path.getmtime("/Volumes/VOLUME1/DCIM/100MEDIA/"+filer)))
	note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
	note.content += '<en-note>'

	#os.path.getmtime(file)
	
	# To include an attachment such as an image in a note, first create a Resource
	# for the attachment. At a minimum, the Resource contains the binary attachment
	# data, an MD5 hash of the binary data, and the attachment MIME type.
	# It can also include attributes such as filename and location.
	image = open("/Volumes/VOLUME1/DCIM/100MEDIA/"+filer, 'rb').read()
	md5 = hashlib.md5()
	md5.update(image)
	hashi = md5.digest()
	hashis = md5.hexdigest()
	print str(hashis)
	note.content+= '<en-media type="image/jpeg" hash="'+str(hashis)+'" /></en-note>'
	data = Types.Data()
	data.size = len(image)
	data.bodyHash = hashi
	data.body = image
	
	resource = Types.Resource()
	resource.mime = 'image/jpeg'
	resource.data = data
	
	# Now, add the new Resource to the note's list of resources
	note.resources = [resource]
	notenew = noteStore.createNote(note)
	os.remove("/Volumes/VOLUME1/DCIM/100MEDIA/"+filer)

#import hashlib
#import binascii
#import evernote.edam.userstore.constants as UserStoreConstants
#import evernote.edam.type.ttypes as Types

