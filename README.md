# Webfortune
This is my Dev Ops final webfortune app. It is a flask app that uses 'cowsay' and 'fortune' as input onto the screen. I have dockerized it for better install.

#Building Docker Image

`docker build -t webfotune`

#Running The App
To run the app locally: 
`docker run -it webfortune`
`python3 -m flask run --host=0.0.0.0`

To run the app through Docker:
`run -dp <CONTAINER_PORT>:5000 webfortune`

#Testing App
To test app:
`pytest test_appserver.py`
