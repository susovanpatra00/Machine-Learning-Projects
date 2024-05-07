from flask import Flask,render_template,request
import pickle

app = Flask(__name__, static_url_path='/GIF')


pipe = pickle.load(open("Model/Naive_model.pkl","rb"))

@app.route('/', methods=["GET","POST"])
def main_function():
    if request.method == "POST":
        text = request.form
        emails = text['email']
        print(emails)
        
        list_email = [emails]
        output = pipe.predict(list_email)[0]
        print(output)


        return render_template("show.html", prediction = output)
    
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)