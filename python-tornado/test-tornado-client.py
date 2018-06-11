import urllib.request
import threading
base_url = "http://127.0.0.1:8888/video/example"



class MyTread(threading.Thread):
    def __init__(self, arg):
        super(MyTread, self).__init__()
        self.arg = arg
    
    def run(self):
        response = urllib.request.urlopen(base_url)
        print(self.arg+"\n"+response.read().decode('utf-8'))


for i in range(10):
    t = MyTread(str(i))
    t.start()





