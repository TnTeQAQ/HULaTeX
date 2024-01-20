from flask import Flask, render_template, jsonify, request
import config
import shutil
import subprocess
import os

app = Flask(__name__, static_folder=os.getcwd()+'/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/latex', methods=['POST'])
def latex2pdf():
    file = request.files['file']
    try:
        file.save(app.static_folder+'/temp/'+file.filename)
    except:
        print('保存latex文件失败')
        return jsonify({'result': '保存latex文件失败'}), 415
    try:
        latex_file = app.static_folder + '/temp/' + 'temp.tex'
        output_dir = app.static_folder + '/temp/'
        subprocess.run(['pdflatex', latex_file], cwd=output_dir, timeout=4.5)
        subprocess.run(['pdflatex', latex_file], cwd=output_dir)
        shutil.copy(latex_file, output_dir+'lastchange.tex')
    except:
        print('转换失败')
        return jsonify({'result': '转换失败'}), 415
    return jsonify({'result': '成功'}), 200


if __name__ == '__main__':
    app.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)