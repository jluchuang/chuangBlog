from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import qrcode
from cStringIO import StringIO

def generate_qrcode(request) : 
	img = qrcode.make("www.keeptry.cn")

	buf = StringIO()
	img.save(buf)
	image_stream = buf.getvalue()

	response = HttpResponse(image_stream, content_type = "image/png")
	response['Last-Modified'] = 'Wed, 22 July 2015 15:02 GMT'
	response['Cache-Control'] = 'max-age=31536000'
	return response
