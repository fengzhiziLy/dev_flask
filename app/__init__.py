"""初始化app核心对象
配置相关的一些插件
"""

from flask import Flask

from app.config import config, DevelopmentConfig

app = Flask(__name__)

# config = DevelopmentConfig


def create_app():
    """初始化"""
    # 初始化数据库
    # 配置文件
    app.config.from_object(config)
    # 自定义的错误处理机制
    # 模板过滤器注册
    return app
