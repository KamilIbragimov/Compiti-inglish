from flask import Flask, request, render_template

app = Flask(__name__)

#rerer


@app.route('/', methods=['GET', 'POST'])
def gg():
    if request.method == 'POST':
          
       
        username = request.form.get('username')
        email    =request.form.get ('email')
        password = request.form.get('password')

        return ("form.html")
    


if __name__ == "__main__":
    app.run(debug=True, port=6989)
       

