import io
from picamera import PiCamera
from time import sleep
import json
import base64
import requests
from google.cloud import storage
import googleapiclient.discovery
import datetime
import time

camera = PiCamera()
service = googleapiclient.discovery.build('storage', 'v1')
storage_client = storage.Client()
bucket = storage_client.get_bucket('restaurants_psu')


blob = bucket.blob('waits/bagelcrust')


def takepic():		
	#camera.start_preview()
	sleep(15)

	camera.capture('/home/pi/com.jb.pronto/images/cam.jpg')
	#camera.stop_preview()

def sendpic():
	data = {}
	data['name'] = 'bagelcrust'
	
	image = open('/home/pi/com.jb.pronto/images/cam.jpg', 'rb')
	image_read = image.read()
	image_64_encode = base64.encodestring(image_read)
	
	data['img'] = image_64_encode
	
	with open('bagelcrust.json', 'w') as outfile:  
		json.dump(data, outfile)	

	json_data = json.dumps(data)

	blob.upload_from_filename('/home/pi/com.jb.pronto/com.jb.pronto/bagelcrust.json')

	
	print('successfully uploaded Bagel Crust picture')
        
        


def main():
	while datetime.datetime.now().hour >7 or datetime.datetime.now().hour < 1: 

		print(str(datetime.datetime.now().hour))	
		takepic()	
		sendpic()
	
main()
