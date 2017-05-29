#!flask/bin/python
from app import app
app.run(debug=True, port=3000   , host="192.168.1.8", threaded=False,use_reloader=False)