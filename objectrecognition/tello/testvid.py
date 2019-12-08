import socket
tello_ip = ""
tello_video_port=
local_ip = ""
local_port=
class Tello:
    def __init__(self, tello_ip, video_port,local_ip,local_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((local_ip, local_port))

        self.tello_ip = tello_ip
        self.tello_port = 
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log = []

        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        

