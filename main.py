import cherrypy

class MySite(object):
    
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = 'https://4200-racitifilip-960esercita-fo343xmn9v5.ws-eu97.gitpod.io'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'ngrok-skip-browser-warning'    
        #cherrypy.response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
        #cherrypy.response.headers['Access-Control-Allow-Credentials']=  "true"
        return {'x':'ciao'}
    
    @cherrypy.expose    
    def ciao(self):
        return 'ciao a tutti'
    

cherrypy.quickstart(MySite())