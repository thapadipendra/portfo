from flask import Flask ,render_template ,url_for,request,redirect,make_response
import csv
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
    
def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer=csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return render_template("thankyou.html")
        except:
            return "didn't save to database"    
    else:
        return "something is wrong"    
    
