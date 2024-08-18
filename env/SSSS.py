from flask import Flask 

app = Flask(__name__)

tutorials = [
    {
        'title':'1'
    },
    {
        'title':'2'
    }
]

@app.route('/tutorials', methods=['GET'])
def get_list():
    return 
