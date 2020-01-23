from flask import Flask, jsonify, request
import subprocess
import random
import string

app = Flask(__name__)

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route('/run', methods=['POST'])
def home():

    code = request.data

    print(code)

    rand = randomString()
    fileName = rand + '.py'
    outName = fileName + '.txt'

    f = open(fileName, "w+")
    f.write(code.decode("utf-8"))
    f.close()

    with open(outName, "w+") as output:
      subprocess.call(["python", "./"+fileName], stdout=output, stderr=output)

    with open(outName, 'r') as content_file:
      result = content_file.read()

    return result

@app.route('/')
def test():
  return 'test success'

app.run()
