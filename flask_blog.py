from flask import Flask, render_template

app = Flask(__name__)

posts =[
    {
    'title':'me',
    'date':90    
    },
    {
    'title':'you',
    'date':10    
    },
    {
    'title':'he',
    'date':20    
    }
]


@app.route("/")
def hello():
    return render_template('home.html', tit="Meti",posts=posts)
@app.route("/about")
def m():
    return render_template('about.html')

 
if __name__ == '__main__':
    app.run(debug=True)