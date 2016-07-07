from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/tasks/', methods=['GET' , 'POST'])

def index():
    # """ Displays the index page accessible at '/'
    # """
    # return render_template('index.html')
    if request.method == 'POST':
        tts = request.form['tts']
        flash(str(tts)+'is being selected')
   
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

  