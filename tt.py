from werobot import WeRoBot

robot = WeRoBot(token='MyToken')


@robot.handler
def hello(message):
    return 'Hello World!'

from bottle import Bottle
from werobot.contrib.bottle import make_view

app = Bottle()
app.route(
    '/',  # WeRoBot 挂载地址
    ['GET', 'POST'],
    make_view(robot)
)

app.run(port=8888)