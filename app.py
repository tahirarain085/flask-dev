from flask import Flask, render_template,request

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route('/')
def home():
    return render_template('home.html')

@app.get('/about')
def about():
    return render_template('about.html',title = "about")

@app.errorhandler(404)
def handle_404(e):
    return render_template("status_404.html"),404


if __name__ == "main":
    # run flask app here
    app.run(host='0.0.0.0',debug=False,port=8000)