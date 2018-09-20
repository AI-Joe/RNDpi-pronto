from picamera import PiCamera
from time import sleep
import json
import base64
from google.cloud import storage
import googleapiclient.discovery
import datetime


'''Takes picture of line using Raspberry Pi.
Parameters:
	none
Returns:
	nothing'''
def take_pic():
	sleep(15)
	try:
		camera.capture('/home/pi/com.jb.pronto/images/cam.jpg')
	except:
		print('Camera failed to get picture!')


'''Opens image and encodes it 
Parameters:
	none
Returns:
	encoded data (name and picture)'''
def open_pic():
	data = {}
	data['name'] = 'bagelcrust'
	image = open('/home/pi/com.jb.pronto/images/cam.jpg', 'rb')
	image_read = image.read()
	image_64_encode = base64.encodestring(image_read)
	data['img'] = image_64_encode

	return data


'''Encodes and uploads picture of line to file
Parameters:
	data - dictionary of encoded picture data
Returns:
	nothing'''
def send_pic(data):
	with open('bagelcrust.json', 'w') as outfile:  
		json.dump(data, outfile)	
	json_data = json.dumps(data)

	blob.upload_from_filename('/home/pi/com.jb.pronto/com.jb.pronto/bagelcrust.json')

	print('successfully uploaded Bagel Crust picture')


'''Main function'''
def main():
	current_hour = datetime.datetime.now()
	while current_hour.hour >= 7 or current_hour.hour <= 1:
		print('The hour is', current_hour.hour)
		take_pic()
		pic_data = open_pic()
		send_pic(pic_data)


'''Sets up RaspberryPi Camera and storage for pictures'''
camera = PiCamera()
service = googleapiclient.discovery.build('storage', 'v1')
storage_client = storage.Client()
bucket = storage_client.get_bucket('restaurants_psu')
blob = bucket.blob('waits/bagelcrust')

'''Calls main function'''
main()
