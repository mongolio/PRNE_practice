class NetworkDevice(object):

    def __init__(self,name = "R1",ip = "192.168.1.12", user="cisco", pw="cisco"):
        self.name = name
        self.os = "Unknown"
        self.ip = ip
        self.user = user
        self.pw = pw
        self.__level = "critical"


class IOSDevice(NetworkDevice):

    def __init__(self,name,ip,user,pw):
        super(IOSDevice, self).__init__(name,ip,user,pw)
        self.os = "Cisco IOS-XE"

    def print_level(self):
        print self.__level

class XRDevice(NetworkDevice):

    def set_os(self):
        self.os = "Cisco IOS-XR"

device = IOSDevice("R1","10.0.0.1","mongol","ololo")
device.print_level()

