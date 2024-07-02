from flask import Flask

app = Flask("AS Gatineau")

@app.router('/')  #route par de default
def acceuil():
    return "ESSAY: / "

# on lance notre web app en mode serveur
app.run(host="0.0.0.0", port=3809)


    