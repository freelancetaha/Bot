import os
from datetime import datetime

# User Configuration
USER = "freelancetaha"
START_TIME = "2025-02-10 06:27:29"

# App Configuration
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 1800

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}