# Initialize flask app
import base64

import cv2
from flask import Flask, render_template, Response, make_response, request

app = Flask(__name__)

#Initialize camera
# camera = cv2.VideoCapture(0)

#
# # Adding window and generating frames from the camera
# def gen_frames():
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             frame = cv2.resize(frame, (1, 1))
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             print("frame", frame)
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame on
#


# Define a route for the default URL, which loads the form
@app.route('/')
def index():
    return render_template('index.html')

# Define app rout for the video feed
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/save_photo', methods=['GET', 'POST'])
def save_photo():
    # take photo and save to png
    # success, frame = camera.read()
    # print("success", success)
    # print("frame", frame)

    print(request)
    print(request.data)

    image_data = request.data

    image_data = image_data.split(b',')[1]
    image_data = base64.b64decode(image_data)
    with open('templates/photos/image.png', 'wb') as f:
        f.write(image_data)
    return 'Successfully saved image'

    success = True
    if success:
        # cv2.imwrite('photo.png', frame)
        return make_response('success')
    else:
        return make_response('fail')

if __name__ == "__main__":
    app.run(debug=True)