from flask import Flask, request, render_template
app = Flask(__name__)

from commons import get_model
from inference import read_image
from inference import time
from inference import test_single_image
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html', value='hi')
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			print('file not uploaded')
			return
		file = request.files['file']
        	# Save the file to ./uploads
		#basepath = os.path.dirname(__file__)
		#img_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
		#print(img_path)
		#file.save(img_path)
		bulbimage = file.read()
		print(bulbimage)
		bulbpreds,final = test_single_image(path=bulbimage)
		test_single_image(path=bulbimage)
		return render_template('index.html', bulb=bulbpreds,finalpred=final)

if __name__ == '__main__':
	app.run(debug=True)