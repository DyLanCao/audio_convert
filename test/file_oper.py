
class file_operation(object):
    def __init__(self):
        self.flag = TRUE
    def file_read(self,file_name):
        print("file read")
        wfile = open(file_name,'r')
        print(wfile.read())
        wfile.close()





