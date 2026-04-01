export default function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, password } = req.body || {};

  if (!name || !password) {
    return res.status(400).json({ error: 'Name and password are required' });
  }

  return res.status(201).json({ message: `User ${name} created successfully` });
}
