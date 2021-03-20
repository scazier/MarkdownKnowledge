import os
from flask import Flask, render_template, request
from flaskext.markdown import Markdown
#import markdown2

app = Flask(__name__)

baseDir = "./content/"

content = ""
with open(baseDir+'index.md', 'r') as f:
    content = f.read()


@app.route("/")
def index():
    return render_template('layout.html', content=content.strip())

@app.route('/<path:path>', methods=['POST','GET'])
def serve_file(path):
    if path[-1] == '/':
        path = path[:-1]
    print(baseDir+path+'.md')
    if os.path.isfile(baseDir+path+'.md'):

        content = ""

        if request.method == 'POST':
            updated_content = request.form['content']
            with open(baseDir+path+'.md','w') as f:
                f.write(updated_content)

        with open(baseDir+path+'.md','r') as f:
            content = f.read()
            
        return render_template('layout.html', content=content.strip(), path='/'+path)
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)
