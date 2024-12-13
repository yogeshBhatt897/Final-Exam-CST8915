from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory staff data
staff_data = {}
current_id = 1

# Create a new staff member
@app.route('/staff', methods=['POST'])
def create_staff():
    global current_id
    data = request.json
    staff_id = current_id
    staff_data[staff_id] = {
        "id": staff_id,
        "name": data.get("name"),
        "position": data.get("position"),
        "department": data.get("department"),
        "email": data.get("email"),
        "phone": data.get("phone")
    }
    current_id += 1
    return jsonify(staff_data[staff_id]), 201

# Read all staff members
@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(list(staff_data.values()))

# Read a specific staff member
@app.route('/staff/<int:staff_id>', methods=['GET'])
def get_staff(staff_id):
    staff = staff_data.get(staff_id)
    if not staff:
        return jsonify({"error": "Staff member not found"}), 404
    return jsonify(staff)

# Update a staff member
@app.route('/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    staff = staff_data.get(staff_id)
    if not staff:
        return jsonify({"error": "Staff member not found"}), 404
    data = request.json
    staff.update({
        "name": data.get("name", staff["name"]),
        "position": data.get("position", staff["position"]),
        "department": data.get("department", staff["department"]),
        "email": data.get("email", staff["email"]),
        "phone": data.get("phone", staff["phone"])
    })
    return jsonify(staff)

# Delete a staff member
@app.route('/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    if staff_id not in staff_data:
        return jsonify({"error": "Staff member not found"}), 404
    del staff_data[staff_id]
    return jsonify({"message": "Staff member deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
