from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [
  {
    'id': 1,
    'service': 'IT Consulting',
    'Description': 'TODO'
  },
  {
    'id': 2,
    'service': 'Website Host/Build',
    'Description': 'TODO'
  },
  {
    'id': 3,
    'service': 'Computer Repair/Installation',
    'Description': 'TODO'
  },
  {
    'id': 4,
    'service': 'Network Installation/Troubleshooting',
    'Description': 'TODO'
  }
]

@app.route("/")
def KND():
    return render_template('home.html', service=SERVICES)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)