from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("patterns.html")

@app.route('/findMatch', methods= ['POST','GET'])
def findMatch():
    patt = re.compile(str(request.form["pattern"]))
    text = str(request.form["textValue"])
    
    matches = re.finditer(patt,text)

    match_list = []
    for match in matches:
        match_list.append(match.group())

    Notfound = True if len(match_list)==0 else False
    return render_template("patterns.html", match_list=match_list, Notfound = Notfound)

@app.route('/checkMail')
def checkMail():
    return render_template("mail.html")

@app.route('/validate', methods=['POST','GET'])
def validate():
    mail_pattern = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    mail_ID = str(request.form["mail"])
    valid = re.match(mail_pattern, mail_ID)

    result = mail_ID + ' is a valid Email ID' if valid else mail_ID + ' is not a valid Email ID'
    return render_template('mail.html', result = result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)