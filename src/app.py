from flask import Flask
from config import config
from flask_cors import CORS

#Routes
from routes import movie

app=Flask(__name__)

CORS(app,resources={"*":{"origins":"http:/localhost:9300"}})

def page_not_found(error):
    return "<h1>Not Found Page </h1>",404

if __name__=='__main__':
   app.config.from_object(config['development'])
   
   #BluePrints
   app.register_blueprint(movie.main, url_prefix='/api/movies') 
   
#Error Handlers
   app.register_error_handler(404,page_not_found)
   app.run()