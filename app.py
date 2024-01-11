import socketio

# create instance of socketio that you just imported
#there are two types of server this standard and async which we will learn later
sio = socketio.Server()
#works with events handlers
#ex. when client connects/disconnects

app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})
# used to connect to wsgi webserver


# couple ways to define events handlers
# most convenitent is event decorator
@sio.event
def connect(sid, environ):
    print(sid, 'connected')

@sio.event
def disconnect(sid):
    print(sid, 'disconnected')
# need to take socketio application and transfer to wsgi app that can interact with something like gunicorn
#socketio has wsgiapp create instance above
