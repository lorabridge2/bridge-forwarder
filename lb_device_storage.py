import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

group_name = "lb_devices"

def lb_device_exists(ieee_id):

   values = r.hgetall(group_name)

   values_decoded = {key.decode('utf-8'): value.decode('utf-8') for key, value in values.items()}

   return ieee_id in list(values_decoded.values())

def backup_device_list():

   values = r.hgetall(group_name)

   lb_devices = {key.decode('utf-8'): value.decode('utf-8') for key, value in values.items()}

   with open('lb_devices.json','w') as fp:
      json.dump(lb_devices, fp)

def add_lb_device(ieee_id):

   if lb_device_exists(ieee_id):
      return

   all_keys = list(values_decoded.keys())

   new_key = 1

   if len(all_keys) > 0:

      all_keys_int = [ int(x) for x in all_keys ]

      new_key = max(all_keys_int)+1

   r.hset(group_name, ieee_id, new_key)

   # TODO: Would be a good idea to backup the list in case someone wants to restore the bridge after a catastrophic failure

   #backup_device_list()