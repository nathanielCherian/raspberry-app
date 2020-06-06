from flask import Flask, render_template
from humiture import read_dht11_dat

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/humiture')
def humi():

    result = read_dht11_dat()
    if result:
        humidity, temperature = result
        return render_template('humiture.html', humidity=humidity, temperature=temperature)
    else:
        return render_template('humiture.html', humidity='N/A', temperature='N/A')
    return 'this is a test'



    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
