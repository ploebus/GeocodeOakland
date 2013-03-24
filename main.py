from framework import bottle
from framework.bottle import route, run, template, static_file

@route('/GeocodeOakland')
def welcome():
    output = template('templates/welcome')
    return output

@route('/stlyes/<filename>')
def server_static(filename):
    return static_file(filename, root='/styles')

run(host='localhost', port=8080,reloader=True, debug=True)
