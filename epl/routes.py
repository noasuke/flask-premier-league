from epl import app

@app.route('/')
def index():
  return 'Hello From Flask!'