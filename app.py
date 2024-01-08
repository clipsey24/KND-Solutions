from flask import Flask, jsonify, render_template

app = Flask(__name__)

SERVICES = [
  {
    'id': 1,
    'service': 'IT Consulting',
    'Description': ' Assess existing IT infrastructures, identify areas for improvement, and offer strategic recommendations to enhance efficiency, security, and overall performance.'
  },
  {
    'id': 2,
    'service': 'Website Host/Build',
    'Description': 'Website hosting and building encompass the processes involved in creating and managing a website'
  },
  {
    'id': 3,
    'service': 'Computer Repair/Installation',
    'Description': 'Computer repair and installation involve addressing hardware and software issues, as well as setting up new systems to ensure they function optimally.'
  },
  {
    'id': 4,
    'service': 'Network Installation/Troubleshooting',
    'Description': 'Network installation and troubleshooting involve setting up and maintaining the infrastructure that allows devices to communicate and share information within an organization or across multiple locations.'
  }
]

@app.route("/")
def KND():
    return render_template('home.html', service=SERVICES)

@app.route("/api/service")
def list_services():
  return jsonify(SERVICES)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)