from flask import Flask

app = Flask(__name__)
#1. pagina do site 

#route = link

@app.route("/")

#função

def homepage():
    return "asdfghjklçerfgyuizxcvbnm"


#colocar site no ar

if __name__ == "__main__":
    app.run(debug=True)