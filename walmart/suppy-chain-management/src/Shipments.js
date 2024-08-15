import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

const Shipments = () => {
  const [shipments, setShipments] = useState([]);

useEffect(() => {
  const interval = setInterval(() => {
    axios.get('http://127.0.0.1:5000/api/shipments')
      .then(response => setShipments(response.data))
      .catch(error => console.error('There was an error fetching the shipment data!', error));
  }, 5000);

  return () => clearInterval(interval);
}, []);

  return (
    <div className="container mt-4">
      <h1>Real-Time Shipment Tracking</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Shipment ID</th>
            <th>Origin</th>
            <th>Destination</th>
            <th>Current Location</th>
            <th>Status</th>
            <th>ETA</th>
          </tr>
        </thead>
        <tbody>
          {shipments.map(shipment => (
            <tr key={shipment.id}>
              <td>{shipment.id}</td>
              <td>{shipment.shipment_id}</td>
              <td>{shipment.origin}</td>
              <td>{shipment.destination}</td>
              <td>{shipment.current_location}</td>
              <td>{shipment.status}</td>
              <td>{shipment.eta}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Shipments;
