import random
from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def helloworld():
    return render_template("home.html")

@app.route('/generate')
def generate():
    randquote= None
    with open("quotes.txt", "r", encoding="utf8") as fd:
            
            for i, line in enumerate(fd, start=1):
                if (random.randint(1,i)==1):
                    randquote= line.strip()
    if randquote is None:
        randquote = "No quotes found."
    return render_template("quotes.html",
    quote=randquote)

if __name__=="__main__":
    app.run(debug=True)