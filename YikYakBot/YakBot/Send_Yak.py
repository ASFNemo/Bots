import socket
import json

class Send_Yak(object):
    '''
        This Class is for creatign the JSON object, connecting to the server and then sending the JSON representation of
        the YAk information to the server to store it.
    '''

    def __init__(self):
        HOST = "127.0.0.1"
        PORT = 10007

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

    def send_Yak(self, yak, upvotes, image):

        yak_json = self.create_Json(yak, upvotes, image)
        print yak_json

        self.socket.send(yak_json +"\n")

    def create_Json(self, yak, upvotes, image):
        data_dict = {'yak':yak, 'img':image, 'upvotes':upvotes}

        JSON_obj = json.dumps(data_dict)
        print JSON_obj

        return JSON_obj
