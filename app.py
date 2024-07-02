from flask import Flask

app = Flask("__name__")

@app.route('/')  #route par de default
def acceuil():
    return ('/Acceuil.html')



if __name__ == "__main__":
    app.run(debug=True)













# on lance notre web app en mode serveur
#app.run(host="0.0.0.0", port=3809)