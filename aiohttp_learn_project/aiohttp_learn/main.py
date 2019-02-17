from aiohttp import web
from routers import setup_routes
#from settings import config
import aiohttp_jinja2
import jinja2
from middlewares import setup_middlewares

app = web.Application()

aiohttp_jinja2.setup(app, 
            loader=jinja2.FileSystemLoader(['./templates',
                                            './aiohttp_learn/templates',
                                            './aiohttp_learn_project/aiohttp_learn/templates']))

setup_routes(app)
setup_middlewares(app)
#app['config'] = config
web.run_app(app, host='127.0.0.1', port=5153)