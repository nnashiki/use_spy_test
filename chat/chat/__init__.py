__version__ = '0.1.0'

def external_method():
    return "hoge"

class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        external_method()
        return sent_message
