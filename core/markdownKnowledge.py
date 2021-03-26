import os
import utils
from flask import Flask, render_template, redirect, request, send_from_directory, jsonify
from flaskext.markdown import Markdown
#import markdown2

app = Flask(__name__)

baseDir = "./content/"

@app.route("/")
def index():
    return render_template('layout.html', content=open(baseDir+'index.md', 'r').read().strip(), isContent=False)

@app.route('/favicon.ico')
def favicon():
    #return send_from_directory(os.path.join(app.root_path, 'static'),
    #                           'favicon.ico', mimetype='image/vnd.microsoft.icon')
    pass

@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'GET':
        directories = utils.list_directories(baseDir)
        return render_template('create.html', directories=directories)
    else:
        filename = request.form['filename']
        dirPath = request.form['directory-path']
        newDirName = '/'+request.form['new-directory-name']+'/' if request.form.get('isInNewDirectory') != [] else ''

        filePath = dirPath+newDirName
        if newDirName != '':
            os.mkdir('./content/'+filePath)
            utils.create_summary('./content/'+filePath+'/')

        with open('./content/'+filePath+'/'+filename+'.md','w') as f:
            f.write("<h1 align=\"center\" style=\"font-size:60px\">"+filename+"</h1>")

        return redirect(filePath+filename)

@app.route('/checkName', methods=['POST'])
def checkName():
    name = request.form['name']
    data = {'res': 1}

    if name in utils.list_files(baseDir):
        data['res'] = 0

    return jsonify(data)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['search']
    files = utils.search(keyword)

    return render_template('search.html', files=files)

@app.route('/<path:path>', methods=['POST','GET'])
def serve_file(path):
    if path[-1] == '/':
        path = path[:-1]

    if path.split('/')[-1] == 'index':
        print(baseDir+path.replace('index',''))
        utils.create_summary(baseDir+path.replace('index',''))

    if os.path.isfile(baseDir+path+'.md'):
        content = ""

        if request.method == 'POST':
            updated_content = request.form['content']
            with open(baseDir+path+'.md','w') as f:
                f.write(updated_content)

        with open(baseDir+path+'.md','r') as f:
            content = f.read()
            
        return render_template('layout.html', content=content.strip(), path='/'+path, isContent=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
