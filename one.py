from flask import Flask
app = Flask(__name__)
@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return ("sel.name")
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it
