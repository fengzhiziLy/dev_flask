"""web服务器
选用 gunicorn uwsgi waitress
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
