
// server.js
// Run: npm init -y && npm install express body-parser helmet cors
// then: node server.js
const express = require('express');
const bodyParser = require('body-parser');
const helmet = require('helmet');
const cors = require('cors');

const app = express();
app.use(helmet());
app.use(cors()); // configure origin in production
app.use(bodyParser.json());

// Simple in-memory store: { phone: { lat, lon, accuracy, timestamp } }
const locations = new Map();

// Middleware placeholder: simple API key check (replace with proper auth)
function requireApiKey(req, res, next) {
  // Example: clients must include header x-api-key: secret123
  const key = req.header('x-api-key');
  if (!key || key !== process.env.API_KEY) {
    return res.status(401).send('Unauthorized');
  }
  next();
}

/**
 * POST /reportLocation
 * Body: { phone, lat, lon, accuracy?, timestamp? }
 * This endpoint is intended to be called by the consenting user's device.
 */
app.post('/reportLocation', (req, res) => {
  const { phone, lat, lon, accuracy, timestamp } = req.body || {};
  if (!phone || typeof lat !== 'number' || typeof lon !== 'number') {
    return res.status(400).send('Missing or invalid fields');
  }

  // Validate inputs more strictly in production
  locations.set(phone, {
    lat, lon, accuracy: accuracy || null,
    timestamp: timestamp || new Date().toISOString()
  });

  return res.status(200).send('Location saved');
});

/**
 * GET /location/:phone
 * Protected endpoint: returns last known location for a phone number.
 * In production: require proper auth + verify requester has permission.
 */
app.get('/location/:phone', requireApiKey, (req, res) => {
  const phone = req.params.phone;
  const record = locations.get(phone);
  if (!record) return res.status(404).send('No location for that number');

  // Optionally mask precision or age of data based on requester's permission
  return res.json({
    phone,
    ...record
  });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(Location server running on port ${port});
});