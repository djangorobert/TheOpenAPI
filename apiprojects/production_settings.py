from settings import *

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "nvm/frontend"),
]

WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR, 'nvm/webpack-stats.prod.json'),
        }
}