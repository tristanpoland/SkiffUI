from flask import Flask, render_template
from nodezator import *

app = Flask(__name__)

class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children


# Define the nodes
node1 = Node('Node 1', [])
node2 = Node('Node 2', [])
node3 = Node('Node 3', [node1, node2])
node4 = Node('Node 4', [node3])
nodes = [node1, node2, node3, node4]

@app.route('/')
def index():
    return render_template('index.html', nodes=nodes)

if __name__ == '__main__':
    app.run(debug=True)