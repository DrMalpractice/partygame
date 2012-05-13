from flask import Flask

app = Flask(__name__)
app.config.from_object('partygame.config')
app.config.from_envvar('PARTYGAME_SETTINGS', silent=True)

import partygame.views
