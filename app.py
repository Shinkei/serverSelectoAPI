# app.py
import http.client
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    """Example fot the default endpoint
    """
    return "<h1>Server Selector API</h1>"


@app.route('/getRegions/', methods=['GET'])
def getRegions():
    """Get the list of regions available

      Returns:
          List:list of strings representing the region names
    """
    response = fetchAivenCloudData()
    servers = json.loads(response)['clouds']

    response = []

    for server in servers:
        if server['geo_region'] not in response:
            response.append(server['geo_region'])

    response.sort()

    return jsonify(response)


@app.route('/getServers/', methods=['GET'])
def getAllServers():
    """Get the list of all servers availables

      Returns:
          List:list of all the servers available to choose
    """
    response = fetchAivenCloudData()
    servers = json.loads(response)['clouds']

    return jsonify(servers)


@app.route('/getServers/<region>', methods=['GET'])
def getServersByRegion(region):
    """Get the list of regions available

      Args:
          region: name of the region

      Returns:
          List:list of servers in a specifiv region
    """
    response = fetchAivenCloudData()
    servers = json.loads(response)['clouds']

    response = []

    for server in servers:
        if server['geo_region'] == region:
            response.append(server)

    return jsonify(response)


def fetchAivenCloudData():
    """ fetch the aiven cloud API """
    conn = http.client.HTTPSConnection("api.aiven.io")

    conn.request("GET", "/v1/clouds")

    res = conn.getresponse()
    data = res.read()

    response = data.decode("utf-8")
    return response


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
