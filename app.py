import sys
import cherrypy

class Hello(object):
	@cherrypy.expose
	@cherrypy.tools.response_headers(headers=[('Content-Type', 'text/plain')])
	def index(self):
		message = """\
Hello Azure!
Python: {python_version}
CherryPy: {cherrypy_version}

More info: http://blog.cincura.net/id/233498
"""
		return message.format(python_version=sys.version, cherrypy_version=cherrypy.__version__)


wsgi_app = cherrypy.Application(Hello(), '/')

if __name__ == '__main__':
	from wsgiref.simple_server import make_server

	httpd = make_server('', 6600, wsgi_app)
	httpd.serve_forever()