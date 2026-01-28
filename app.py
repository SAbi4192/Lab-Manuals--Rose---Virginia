from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (for demonstration purposes)
data = [
    {"id": 1, "name": "Item 1", "description": "This is the first item."},
    {"id": 2, "name": "Item 2", "description": "This is the second item."},
    {"id": 3, "name": "Item 3", "description": "This is the third item."}
]

# 1. GET: Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# 2. POST: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    item = request.get_json()
    data.append(item)
    return jsonify({"message": "Item created successfully"})

# 3. PUT: Update an existing item
# Note: uses the item_id as the list index (0, 1, 2...)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(data):
        updated_item = request.get_json()
        data[item_id] = updated_item
        return jsonify({"message": "Item updated successfully"})
    else:
        return jsonify({"message": "Item not found"}), 404

# 4. DELETE: Remove an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(data):
        del data[item_id]
        return jsonify({"message": "Item deleted successfully"})
    else:
        return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)