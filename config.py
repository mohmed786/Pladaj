class Config(object):
    SECRET_KEY = "CantStopAddictedToTheShinDigChopTopHeSaysImGonnaWinBig"
    HOST = "6095d71c.ngrok.io"

    SHOPIFY_CONFIG = {
        'API_KEY': 'e857418c0e77115c1b9ec5b84b68c7da',
        'API_SECRET': 'e4d9aa9d182e5eb9b9cd6ea705cf6f59',
        'APP_HOME': 'http://' + HOST,
        'CALLBACK_URL': 'http://' + HOST + '/install',
        'REDIRECT_URI': 'http://' + HOST + '/connect',
        'SCOPE': 'read_script_tags, write_script_tags, read_collection_listings, read_content, write_content'
    }
