from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('supply_chain.db')
    c = conn.cursor()

    # Create a table for shipments
    c.execute('''CREATE TABLE IF NOT EXISTS shipments (
        id INTEGER PRIMARY KEY,
        shipment_id TEXT NOT NULL,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        current_location TEXT,
        status TEXT NOT NULL,
        eta TEXT
    )''')

    conn.commit()
    conn.close()

# Run the init_db function when the app starts
init_db()

# Route to get all shipments
@app.route('/api/shipments', methods=['GET'])
def get_shipments():
    conn = sqlite3.connect('supply_chain.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shipments")
    shipments = c.fetchall()
    conn.close()

    shipment_list = []
    for shipment in shipments:
        shipment_data = {
            "id": shipment[0],
            "shipment_id": shipment[1],
            "origin": shipment[2],
            "destination": shipment[3],
            "current_location": shipment[4],
            "status": shipment[5],
            "eta": shipment[6]
        }
        shipment_list.append(shipment_data)

    return jsonify(shipment_list)

# Route to update a shipment's status or location
@app.route('/api/shipments/<int:shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    conn = sqlite3.connect('supply_chain.db')
    c = conn.cursor()

    new_status = request.json.get('status')
    new_location = request.json.get('current_location')
    new_eta = request.json.get('eta')

    c.execute("UPDATE shipments SET status = ?, current_location = ?, eta = ? WHERE id = ?",
              (new_status, new_location, new_eta, shipment_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Shipment updated successfully"})

# Route to add a new shipment (optional, for testing purposes)
@app.route('/api/shipments', methods=['POST'])
def add_shipment():
    conn = sqlite3.connect('supply_chain.db')
    c = conn.cursor()

    shipment_id = request.json.get('shipment_id')
    origin = request.json.get('origin')
    destination = request.json.get('destination')
    current_location = request.json.get('current_location')
    status = request.json.get('status')
    eta = request.json.get('eta')

    c.execute("INSERT INTO shipments (shipment_id, origin, destination, current_location, status, eta) VALUES (?, ?, ?, ?, ?, ?)",
              (shipment_id, origin, destination, current_location, status, eta))
    conn.commit()
    conn.close()

    return jsonify({"message": "New shipment added successfully"}), 201

# Home route (for testing purposes)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Real-Time Supply Chain Visibility API!"})

if __name__ == '__main__':
    app.run(debug=True)
