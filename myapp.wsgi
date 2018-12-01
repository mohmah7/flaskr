import sys

def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    output =( sys.stderr, 'sys.prefix = %s' % repr(sys.prefix))
    output = ( sys.stderr, 'sys.path = %s' % repr(sys.path))

    return [output]
