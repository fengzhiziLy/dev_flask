class BaseConfig:
    PER_PAGE = 10
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    DEBUG = False


# 方法一
config = DevelopmentConfig()


