from flask import render_template,Blueprint,request
from summarize.summary import get_text_summary
from summarize.TextRank import textRankSummary
from summarize.LexRank import lexRankSummary
import os 

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def get_file():
    return render_template('home.html')

@views.route('/summary',methods=['GET','POST'])
def get_summary():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(os.getcwd(),'webapp','static','uploads')
            file.save(os.path.join(filepath,file.filename))
            print(file.filename)
            summary1 = get_text_summary(file.filename)
            summary3 = textRankSummary(file.filename)
            summary2 = lexRankSummary(file.filename)
            return render_template('home.html',summary1=summary1,summary2=summary2,summary3=summary3)
        
    return render_template('home.html')