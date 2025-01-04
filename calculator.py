from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', current_value='0')

@app.route('/button_click', methods=['POST'])
def button_click():
    current_value = request.form['current_value']
    clicked_value = request.form['clicked_value']
    
    if clicked_value == "=":
        try:
            new_value = eval(current_value)
        except:
            new_value = 'Error'
    elif clicked_value == "C":
        new_value = '0'
    else:
        if current_value == '0':
            new_value = clicked_value
        else:
            new_value = current_value + clicked_value
    
    return render_template('index.html', current_value=new_value)

if __name__ == '__main__':
    app.run(debug=True)
