import os
import sys


devices_list = []

for dev in os.popen("adb devices").readlines():
    dev_id = dev.split('\t')[0]
    if dev_id == ' ':
        pass
    elif '*' in dev_id:
        pass
    elif 'List' in dev_id:
        pass
    elif '\n' in dev_id:
        pass
    else:
        id_cmd = '''adb -s %s shell "cat /system/build.prop | grep ro.build.display.id"''' % dev_id
        dev_name = os.popen(id_cmd).readline().split("=")[-1][:-1]
        if not dev_name:
            dev_name = 'Not authorized'
        devices_list.append((dev_name, dev_id))

if not devices_list:
    print('No device found. Try again')
    sys.exit(1)

devices_list = ['{}({})'.format(i[1], i[0]) for i in devices_list]
device_choice = input('single-list|Please select your device|' + '%'.join(devices_list))

print('Your choice is device {}'.format(device_choice))
