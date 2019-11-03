import flask
from flask import Flask, request, render_template, session, redirect, url_for
import pandas as pd

app=Flask('__main__')

@app.route('/', methods=['GET', 'POST'])
def upload_xml():
    if request.method == 'POST':
        data = pd.read_csv(request.files.get('file'))
        return render_template('upload.html',data=data.to_html(index=False,classes = 'my_class" id = "myTable'))
    return render_template('upload.html',data='')

@app.route("/next",methods=['GET', 'POST'])
def nexpagedisplay(filename):
    return render_template('upload.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5050, threaded=True)
