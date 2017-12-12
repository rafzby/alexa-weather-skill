# Alexa Weather Skill

Alexa weather skill using OpenWeatherMap API.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

This project requires **python3.5**

Create an account on http://openweathermap.org/api and get the **API KEY**.

Create *.env* file in project directory and complete it as below:

```
API_KEY=1234567890ABCDEFGH
CITY=London,UK
```

Obviously put your city there :)

Create *virtualenv* and install requirements.

```sh
virtualenv -p /usr/bin/python3.5 venv

source venv/bin/activate

pip install -r requirements.txt
```

Download *ngrok* https://ngrok.com/

We will use it to test this skill from local machine.

### Configuration

Create an account on https://developer.amazon.com/

In developer console open **ALEXA** tab and click **Get Started** button below **Alexa Skills Kit** tab.

![alexa-weather-skill](https://i.imgur.com/7RkPiit.png)

Then click **Add a New Skill** button.

Complete **Name** and **Invocation Name** as follows:

![alexa-weather-skill](https://i.imgur.com/eKyJJ6V.png)

Click **Save**.

Complete Interaction model with intent schema and utterances. You will find them in project directory.

![alexa-weather-skill](https://i.imgur.com/MUqFAsN.png)

![alexa-weather-skill](https://i.imgur.com/xj5Inax.png)

Run *app.py* and then run *ngrok* to create a tunnel which will expose app to the internet.

```sh
python app.py

ngrok http 5000
```

You should see output like this.

![alexa-weather-skill](https://i.imgur.com/J1Bme7U.png)

Go to the **Configuration** tab in alexa developer console.

Select **HTTPS** endpoint type.

Copy *https* url from your *ngrok* output and paste it in endpoint configuration in alexa developer console.

![alexa-weather-skill](https://i.imgur.com/YIGi43L.png)

