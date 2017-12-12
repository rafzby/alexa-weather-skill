from flask import Flask
from flask_ask import Ask, statement
from services import weather

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('WeatherIntent')
def weather_intent():
    data = weather.get_weather_data()
    response = "Right now in {} is {} degrees".format(data['name'], data['main']['temp'])

    return statement(response)


@ask.session_ended
def session_ended():
    return '{}', 200


if __name__ == '__main__':
    app.run()
