# coding: utf-8
import time
from flask import Flask, request
from flask_restplus import Resource, Api
from flask_cors import CORS
from flask_restful_swagger import swagger
from detector import face_detect


app_name = 'Face detector'
app = Flask(__name__)
api = swagger.docs(Api(version='1.0', 
                       title=app_name, 
                       description='Face detector API', 
                       default_label='Tasks',
                       default='/api/v1'))

def configure_app(app, config=None):
    CORS(app, resources={r'*': {'origins': '*'}})
    api.init_app(app)

@api.route('/detector')
@api.doc(params={'image_url': 'Image url'})
@api.doc(params={'detection_type': 'Strong detection?'})
class Detector(Resource):
    def get(self):
        print("Processing url: {}".format(request.args['image_url']))
        start = time.time()
        image_url = request.args['image_url']
        strong = request.args.get('detection_type')
        detection_type = -1 if strong else 1
        print("Detection type {}".format(detection_type))
        detection = face_detect(image_url, detection_type)
        print("Execution took {:.4f}".format(time.time() - start))
        return detection

@api.route('/ping')
class Health(Resource):
    def get(self):
        return "pong"

if __name__ == '__main__':
    configure_app(app, {'PROJECT': app_name + '-service'})
    app.run(debug=True,host='0.0.0.0')
