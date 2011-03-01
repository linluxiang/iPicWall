#!/usr/bin/python
#encoding:utf8
'''
This is a picture wall for techparty.org

Free for all use

@author: linluxiang@gmail.com
@author-blog: linluxiang.info

'''
from flask import Flask, url_for, render_template, request
import simplejson as sj
import os

##U need to change this two string to your own foler position.
proj_path = '/path_to/iPicWall/'
upload_path = '/path_to/static/upload/'

app = Flask('picwall')
pics = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        s = f.filename[:]
        f.save(''.join([upload_path, s]))
        return 'SUCCESS'
    else:
        return render_template('upload.html')

@app.route('/pics', methods=['GET'])
def getpics():
    global pics
    pics_now = os.listdir(upload_path)
    pics_delta = list(set(pics_now) - set(pics))
    pics = pics_now
    return sj.dumps(pics_delta)

if __name__ == '__main__':
    app.run('0.0.0.0')
