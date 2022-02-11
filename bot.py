from bottle import template, run, route, post, request as bottle_request  # requerimento bottle
import sys
from subprocess import call
import json

@post('/')
def main():  
    data = bottle_request.json  # extrai todo o json
    data1 = json.dumps(data)
    print(data1)
    original_stdout = sys.stdout 
    with open('filename', 'a') as f:
        sys.stdout = f 
        print(data1)
        sys.stdout = original_stdout
    rc = call("./grupo1")
    rc = call("./v3")

    return 

@route('/grupo1') # printa as mensagens do grupo1
def grupo1():
        with open('logtudogrupo1', 'r') as fin:
            return fin.read()


@route('/') #printa todas as msgs 
def home():
    with open('logtudo', 'r') as fin1:
        return fin1.read()


if __name__ == '__main__':  
    run(host='localhost', port=8080, debug=True)
