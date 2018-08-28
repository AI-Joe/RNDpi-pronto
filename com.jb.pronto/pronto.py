import io
from google.cloud import vision
from google.cloud.vision import types
from picamera import PiCamera
from time import sleep

vision_client = vision.ImageAnnotatorClient()

file_name = '/home/pi/com.jb.pronto/images/cam.jpg'
camera = PiCamera()
camera.rotation = -90

camera.start_preview()
sleep(40)
camera.capture('/home/pi/com.jb.pronto/images/cam.jpg')
camera.stop_preview()


with io.open(file_name,'rb') as image_file:
	content = image_file.read()
	image = types.Image(content=content)

response = vision_client.face_detection(image=image)
faces = response.face_annotations

print('There is ' + str(len(faces)) + ' person in the image')
