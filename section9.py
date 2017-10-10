import re
import pprint

OS_versions = {"Cisco IOS":{"count":0,"name":[]},
              "Cisco Nexus":{"count":0,"name":[]},
              "Cisco IOS-XR":{"count":0,"name":[]},
              "Cisco IOS-XE":{"count":0,"name":[]}}

for line in open("devices.txt", "r"):
    device_info = line.split(",")
    if device_info[1] == "ios":
        OS_versions["Cisco IOS"]["count"] += 1
        OS_versions["Cisco IOS"]["name"].append(device_info[0])
    elif device_info[1] == "nx-os":
        OS_versions["Cisco Nexus"]["count"] += 1
        OS_versions["Cisco Nexus"]["name"].append(device_info[0])
    elif device_info[1] == "ios-xr":
        OS_versions["Cisco IOS-XR"]["count"] += 1
        OS_versions["Cisco IOS-XR"]["name"].append(device_info[0])
    else:
        OS_versions["Cisco IOS-XE"]["count"] += 1
        OS_versions["Cisco IOS-XE"]["name"].append(device_info[0])

pprint.pprint(OS_versions)