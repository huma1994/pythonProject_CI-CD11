def application(environ, start_response):
    status = '200 OK'
    output = b'CI CD pipeline using jenkin apache python and developer GIT'

    
    output = b'boom boom'
    response_headers = [('Content-type', 'text/plain'),
    ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
