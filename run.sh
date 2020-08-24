screen -dmS voice
screen -S voice -X stuff 'python3 voice.py\n'
screen -dmS api
screen -S api -X stuff 'uwsgi --http 0.0.0.0:2864 --wsgi-file api.py --callable app\n'
