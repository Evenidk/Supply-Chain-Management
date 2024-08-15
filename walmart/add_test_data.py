import sqlite3

conn = sqlite3.connect('supply_chain.db')
c = conn.cursor()

# Insert test data into the shipments table
c.execute("INSERT INTO shipments (shipment_id, origin, destination, current_location, status, eta) VALUES (?, ?, ?, ?, ?, ?)",
          ('SH001', 'New York', 'Los Angeles', 'Philadelphia', 'In Transit', '2024-08-18'))
c.execute("INSERT INTO shipments (shipment_id, origin, destination, current_location, status, eta) VALUES (?, ?, ?, ?, ?, ?)",
          ('SH002', 'Chicago', 'Houston', 'St. Louis', 'In Transit', '2024-08-20'))

conn.commit()
conn.close()

print("Test data inserted successfully.")
