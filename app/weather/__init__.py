from flask import Blueprint, render_template

weather = Blueprint('weather',
                    __name__,
                    template_folder='templates',
                    static_folder='static')

from . import views
