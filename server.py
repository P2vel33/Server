from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

network_diagram = [
    {
        'id':1,
        'title':"first",
        'discription':"GET, POST routes"
    },
    {
        'id':2,
        'title':"second",
        'discription':"PUT, DELETE routes"
    }
]

@app.route('/network_diagram',methods=["GET"])
def get_list():
    return jsonify(network_diagram)

@app.route('/network_diagram',methods=["POST"])
def update_list():
    new_one = request.json
    network_diagram.append(new_one)
    return jsonify(network_diagram)

@app.route('/network_diagram/<int:network_diagram_id>',methods=["PUT"])
def update_network_diagram(network_diagram_id):
    item = next((x for x in network_diagram if x['id'] == network_diagram_id), None)
    params = request.json
    if not item:
        return{'message: No networks with this id'}, 400
    item.update(params)
    return item

@app.route('/network_diagram/<int:network_diagram_id>',methods=["DELETE"])
def delete_network_diagram(network_diagram_id):
    idx, _ = next((x for x in enumerate(network_diagram) if x[1]['id'] == network_diagram_id), (None, None))
    network_diagram.pop(idx)
    return '', 204

if __name__ == '__main__':
    app.run()
