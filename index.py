from flask import *
import nltk as nl
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/filtered",methods=["GET"])
def filtered():
    data = request.args.get('input')
    nl.download("stopwords")
    cr = []
    cr1 = []
    data = re.sub('[^a-zA-Z]'," ",data)
    data = data.lower()
    data = data.split()
    ps = PorterStemmer()
    data = [word for word in data if not word in set(stopwords.words("english"))]
    cr.append(" ".join(data))
    cr = cr[0].split()
    for i in cr:
        if i not in cr1:
            cr1.append(i)
    
    final_result = " ".join(cr1)
    json_result = {"output":{"response":final_result}}
    return jsonify(json_result)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080",debug=False)