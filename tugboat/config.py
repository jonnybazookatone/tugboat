# encoding: utf-8
"""
Configuration file. Please prefix application specific config values with
the application name.
"""
import os

# Tokens
HARBOUR_CLIENT_ADSWS_API_TOKEN = os.getenv('API_DEV_KEY', '')

# Service URLs
environment = os.getenv('ENVIRONMENT', 'dev')

if environment == 'dev':
    VAULT_QUERY_URL = 'https://devapi.adsabs.harvard.edu/v1/vault/query'
    BUMBLEBEE_URL = 'https://devui.adsabs.harvard.edu'
else:
    VAULT_QUERY_URL = 'https://api.adsabs.harvard.edu/v1/vault/query'
    BUMBLEBEE_URL = 'https://ui.adsabs.harvard.edu'

TUGBOAT_CORS = [
    'adsabs.harvard.edu',
    'astrobib.u-strasbg.fr',
    'ads.nao.ac.jp',
    'ads.astro.puc.cl',
    'esoads.eso.org',
    'ukads.nottingham.ac.uk',
    'ads.iucaa.ernet.in',
    'ads.inasan.ru',
    'ads.bao.ac.cn',
    'ads.mao.kiev.ua',
    'ads.ari.uni-heidelberg.de',
    'ads.arsip.lipi.go.id',
    'ads.on.br',
    'saaoads.chpc.ac.za',
    'adsx.cfa.harvard.edu:8888'
]

# Log settings
TUGBOAT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/tmp/tugboat.log',
        },
        'console': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
