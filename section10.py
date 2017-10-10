device_list = list()

for line in open("devices.txt","r"):
    device_list.append([i.strip() for i in line.split(",") if i])

print "Name     OS-type   IP address           Software          "
print "-------  --------  -------------------  --------------------"
for device in device_list:
    print "{0:8} {1:9} {2:20} {3:20}".format(device[0],device[1],device[2].split(':')[1],device[3])

print ""

#Using While loop
device_list = list()

file = open("devices.txt","r")

line = file.readline()

print "Name     OS-type   IP address           Software          "
print "-------  --------  -------------------  --------------------"

while line:
    device_list.append([i.strip() for i in line.split(",") if i])
    line = file.readline()

i = 0
while i<8:
    device = device_list[i]
    print "{0:8} {1:9} {2:20} {3:20}".format(device[0], device[1], device[2].split(':')[1], device[3])
    i += 1

_set = set([1,2,3])

_set.add(3)
print""
print _set
print ""

#Using break and continue

device_list = list()
ip_addresses = set()
for line in open("devices.txt","r"):
    device_list.append([i.strip() for i in line.split(",") if i])

print "Name     OS-type   IP address           Software          "
print "-------  --------  -------------------  --------------------"

for device in device_list:
    print "{0:8} {1:9} {2:20} {3:20}".format(device[0],device[1],device[2].split(':')[1],device[3]),
    if device[2].split(':')[1] in ip_addresses:
        print '*Duplicate IP!*'
        continue
    ip_addresses.add(device[2].split(':')[1])
    print ""
print ""

print range(5,6)

while True:
    try:
        device_ip = raw_input("'Enter device IP address to find (Ctrl-C to exit):")
    except KeyboardInterrupt:
        break
    for device in device_list:
        if device[2].split(':')[1] == device_ip:
            print "{0:8} {1:9} {2:20} {3:20}".format(device[0], device[1], device[2].split(':')[1], device[3])
            break
    else:
        print "Device not found!"
