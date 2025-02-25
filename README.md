# Bridge Forwarder

This repository is part of the [LoRaBridge](https://github.com/lorabridge2/lorabridge) project.
It provides the docker image for forwarding the data received by zigbee2mqtt used on our bridge device.

The Forwarder is a self-provided Python3 program and listens to message on the Mosquitto server. 
It removes disabled attributes (a list that can be modified via the web interface) and performes a combination of 
key substitution, YAML reformatting and Brotli compression. 
The resulting compressed data is pushed to a list in a Redis server.

## Environment Variables

- `FOR_MQTT_HOST`: IP or hostname of MQTT host
- `FOR_MQTT_PORT`: Port used by MQTT
- `FOR_MQTT_BASE_TOPIC`: MQTT topic used by zigbee2mqtt (default: `zigbee2mqtt`)
- `FOR_REDIS_HOST`: IP or hostname of Redis host
- `FOR_REDIS_PORT`: Port used by Redis
- `FOR_REDIS_DB`: Number of the database used inside Redis
- `FOR_REDIS_LIST`: Name of the list used in redis

## License

All the LoRaBridge software components and the documentation are licensed under GNU General Public License 3.0.

## Acknowledgements

The financial support from Internetstiftung/Netidee is gratefully acknowledged. The mission of Netidee is to support development of open-source tools for more accessible and versatile use of the Internet in Austria.
