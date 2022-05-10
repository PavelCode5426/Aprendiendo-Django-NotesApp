import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_bases={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR+'/database/db.sqlite3',
    }
}