from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    fn = request.form['first_name']
    ln = request.form['last_name']
    sid = request.form['student_id']
    print(f'Charging {fn} {ln} for {int(strawberry) + int(raspberry) + int(apple)} fruits')
    return render_template("checkout.html", apple=apple, raspberry=raspberry, strawberry=strawberry, fn=fn, ln=ln, sid=sid)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    