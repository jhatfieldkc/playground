from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def playground():
    return render_template("index.html", num = 3, background_color = "lightblue")

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("index.html", num = num, background_color = "lightblue")

@app.route('/play/<int:num>/<color>')
def play_num2(num, color):
    return render_template("index.html", num = num, background_color = color )


if __name__=="__main__":
    app.run(debug=True)