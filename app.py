from flask import Flask, render_template, request
from nodezator import Node, Connection, NodeZator

app = Flask(__name__)
node_zator = NodeZator()

@app.route('/')
def index():
    nodes = node_zator.get_nodes()
    connections = node_zator.get_connections()
    return render_template('index.html', nodes=nodes, connections=connections)

@app.route('/add_node', methods=['POST'])
def add_node():
    node_id = request.form['node_id']
    node = Node(node_id)
    node_zator.add_node(node)
    return jsonify({'success': True})

@app.route('/delete_node', methods=['POST'])
def delete_node():
    node_id = request.form['node_id']
    node_zator.delete_node(node_id)
    return jsonify({'success': True})

@app.route('/connect', methods=['POST'])
def connect():
    node_id_1 = request.form['node_id_1']
    node_id_2 = request.form['node_id_2']
    connection = Connection(node_id_1, node_id_2)
    node_zator.add_connection(connection)
    return jsonify({'success': True})

@app.route('/disconnect', methods=['POST'])
def disconnect():
    node_id_1 = request.form['node_id_1']
    node_id_2 = request.form['node_id_2']
    connection = Connection(node_id_1, node_id_2)
    node_zator.delete_connection(connection)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
