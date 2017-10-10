def read_device_file(file_name):
    global device_list
    device_list = [line.split(",") for line in open(file_name)]

def print_device_list():
    global device_list
    print "Name     OS-type   IP address           Software          "
    print "-------  --------  -------------------  --------------------"
    for device in device_list:
        print "{0:8} {1:9} {2:20} {3:20}".format(device[0], device[1], device[2].split(':')[1], device[3])


device_list = []
input_file = "devices.txt"

read_device_file(input_file)
print_device_list()
