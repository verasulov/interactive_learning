import bottle
from src.server import middleware_app, config

from src.routers.api.v1.script.get_script import router_v1_get_script
from src.routers.api.v1.script.create_script import router_v1_create_script
from src.routers.api.v1.script.update_script import router_v1_update_script

from src.routers.api.v1.scripts.get_scripts import router_v1_get_scripts

from src.routers.hook import before_request
from src.routers.core import send_static, index
from src.routers.oauth2 import oauth2_login, oauth2_logout
import src.routers.errors


if __name__ == '__main__':
    server_config = config.get('server', {})

    bottle.run(app=middleware_app, **server_config)
