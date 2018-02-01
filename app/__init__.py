from flask import Flask
from .weather import weather

app = Flask(__name__)

# 在weather.weatherquery.com中添加API蓝图
app.register_blueprint(weather, subdomain='weather')
