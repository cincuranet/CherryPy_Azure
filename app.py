import cherrypy

class Hello(object):
	@cherrypy.expose
	def index(self):
		return "Hello Azure!"


wsgi_app = cherrypy.Application(Hello(), '/')

if __name__ == '__main__':
	from wsgiref.simple_server import make_server

	httpd = make_server('', 6600, wsgi_app)
	httpd.serve_forever()