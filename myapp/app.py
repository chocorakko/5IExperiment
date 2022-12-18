from flask import Flask,render_template,flash,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField,FloatField,SelectField
from wtforms.validators import DataRequired,NumberRange
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
#app.config['SWLALCHEMY_DATABASE_URI'] == 'sqlite:///todo.db'
#db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    form = Ragistration()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['time'] = form.time.data
        if float(form.season.data)!=1.0:
            session['season']=str(float(form.season.data)-1.0)
        else:
            session['season'] = str(float(form.season.data))
        session['now'] = form.now.data
        
        return redirect(url_for('result'))
    return render_template('index.html',form=form)

@app.route('/result')
def result():
    print(type(session['season']))
    return render_template('result.html',name = session['name'],time=float(session['time']),season=float(session['season']),now=session['now'])

class Ragistration(FlaskForm):
    name = StringField('授業名:',validators=[DataRequired()])
    time = IntegerField('1週あたりの授業時間数:',validators=[NumberRange(0,6,'不正な値です')])
    now = FloatField('現時点での欠課時数:',validators=[NumberRange(0,32,'不正な値です')])
    season = SelectField('開設期',choices=[(1,'前期'),(2,'後期'),(3,'通年'),])

    submit = SubmitField('SUBMIT')

if __name__ == "__main__":
    app.run(debug=True)
