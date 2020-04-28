import dash
import dash as dash
import logging as logger
from influxdb import InfluxDBClient

logger.basicConfig(level="DEBUG")

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    client = InfluxDBClient(host="influxdb", port=8086)
    print(client.get_list_database())
    return "hello world"

app.run(host='0.0.0.0',port=5000)

