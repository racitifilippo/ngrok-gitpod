import cherrypy

class MySite(object):
    
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'ngrok-skip-browser-warning'    
        #cherrypy.response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
        #cherrypy.response.headers['Access-Control-Allow-Credentials']=  "true"
        return {'x':'ciao'}
    
    @cherrypy.expose    
    def ciao(self):
        return 'ciao a tutti'
    

cherrypy.quickstart(MySite())
