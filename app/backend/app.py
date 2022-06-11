from flask import Flask, jsonify, request
import json

app = Flask("backend")

nodes = open('/app/public/backend/nodes.json')
edges = open('/app/public/backend/edges.json')
nodeList = json.load(nodes)
edgeList = json.load(edges)

def removeNode(deployment_idx, edge_id):
  for x in edgeList[deployment_idx]:
    s = str(int(edge_id["source"])+1)
    t = str(int(edge_id['target'])+1)
    print(x["source"], s, x["target"], t)
    if(x["source"] == s and x["target"] == t):
      print('founddd')
      edgeList[deployment_idx].remove(x)

@app.route('/deployment')
def processCommand():
  if request.method == 'GET':
    deployment_idx = int(request.args.get('number'))-1
    response = {
      "nodes": nodeList[deployment_idx],
      "edges": edgeList[deployment_idx],
    }
    return jsonify(response)

  if request.method == 'POST':
    return "wrong API call"


@app.route('/summary')
def getSummary():
  return jsonify([len(nodeList)])


@app.route('/deleteEdge', methods=['GET', 'POST'])
def deleteEdge():
  if request.method == 'POST':
    [deployment_idx, edge_id] = request.json
    removeNode(deployment_idx, edge_id)
    response = {
      "nodes": nodeList[deployment_idx],
      "edges": edgeList[deployment_idx],
    }    
    return jsonify(response)

if __name__ == '__main__':
  app.run(debug=False, host="0.0.0.0", port=1027)