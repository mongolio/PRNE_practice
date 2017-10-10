from pprint import pprint
from collections import namedtuple

_llist = [3,4]
device_dict = {}
Dev_info = namedtuple("Dev_info","name os ip user password")
os_types = set()
for line in open("device.txt",'r').readlines():
    device_info = [word.strip() for word in line.split(",") if word]
    #pprint(device_info)
    device_dict[device_info[0]] = ({"os":device_info[1],"ip":device_info[2],"user":device_info[3],"pw":device_info[4]})
pprint(set(device_dict))

#pprint(device_dict)

#def foo(*args):
 #   print type(args)
 #   print args

foo = [3,4,5,3,5,7,"opopo"]
sset = set(foo)
if 3 in sset:
    print sset
print Dev_info
for line in open("device.txt",'r').readlines():
    device_info = Dev_info(*[i.strip() for i in line.split(",")])
    #print device_info

    if device_info.os not in os_types:
        os_types.add(device_info.os)

pprint(os_types)