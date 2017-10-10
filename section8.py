import re


with open("devices.txt","r") as source_file:
   for device_info_list in [line.split(",") for line in source_file if line]:
        device_info = {}
        device_info['name'] = device_info_list[0]
        ip_search_string = re.compile("Mgmt:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})")
        device_info['ip'] = re.search(ip_search_string, device_info_list[2]).group(1)
        device_info['version'] = device_info_list[3]
        print "Device -", device_info['name'], "Management ip address is - ", device_info['ip']
        if device_info['version'] != "Version 5.3.1":
            print "Device -",device_info['name'], "OS version is not current: ",  device_info['version']



vs = 'Cisco IOS XR Software, Version 21.34.685.9'
vp = re.compile('Version ([0-9])*.([0-9])*.([0-9])*.([0-9])*')
vm = vp.search(vs)
v = vm.group(1)
m = re.findall('Version ([0-9])*.([0-9])*.([0-9])*.([0-9])*',vs)
print v
print m


seq = "12345"

print re.search("([0-9])*","12345").group(1)