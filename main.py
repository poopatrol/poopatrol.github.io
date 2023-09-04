
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        name = request.form['text']
        return redirect(url_for('user',name = name))
    return render_template('homepage.html')

# variable URL is possible in <name>
@app.route('/user/<name>')
def user(name):
    return render_template('hello.html', name=name)


# this allows you to run it as a normal python script: no need to use FLASK_APP
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True)

# if you need to avoid using port 5000 - some Mac users -
# delete the first app.run() line above and
# un-comment the second app.run() line. Then use localhost:4999