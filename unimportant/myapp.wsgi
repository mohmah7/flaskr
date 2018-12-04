import sys

def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    #d=  sys.path
    #d=str(d)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    
    #output += d
    #d= sys.path

    return [output]
