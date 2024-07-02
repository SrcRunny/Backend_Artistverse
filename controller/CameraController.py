# controllers/camera_controller.py

from flask import Response, jsonify
from service.CameraService import CameraService
from service.VideoCameraModelService import VideoCamera
class CameraController:
    def __init__(self):
        self.camera_service = CameraService()
        self.video_camera = VideoCamera()

    def video_feed(self):
        print(Response(self.camera_service.gen(), mimetype='multipart/x-mixed-replace; boundary=frame'))
        return Response(self.camera_service.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

    def gen_table(self):
        response = self.camera_service.get_music_recommendations()
        return jsonify(response)
