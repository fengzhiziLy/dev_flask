from app import app


@app.route('/')
def index():
    return 'hello'


'''蓝图
后台系统
前端系统
API接口
application，多个子系统，共享一些配置项：config,g,request，公用一些数据，独立一些组件
不同的地方：返回的数据
蓝图 blueprint() app   类似插座
'''



