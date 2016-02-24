"""Run web app"""

from web import server
from web.config import UI_BIND_HOST, UI_BIND_PORT, UI_DEBUG

if __name__ == '__main__':
    server.app.run(debug=UI_DEBUG, port=UI_BIND_PORT, host=UI_BIND_HOST, threaded=True)
