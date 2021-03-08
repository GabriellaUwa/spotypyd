from flask import Flask
import spotipy
from spotipy import util
from flask import render_template
import model_util
import os

app = Flask(__name__)

clientId = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
callback_uri = os.getenv("CALL_BACK")
scope = "user-library-read"

token = util.prompt_for_user_token(username, scope,
                                   client_id=clientId,
                                   client_secret=clientSecret,
                                   redirect_uri=callback_uri)
my_spot = spotipy.Spotify(token)


@app.route('/', methods=['GET'])
def get_saved_tracks():
    saved_tracks = my_spot.current_user_saved_tracks(limit=50)
    modelled_tracks = model_util.model_track_data(saved_tracks["items"])
    return render_template("home.html", tracks=modelled_tracks)
    # return modelled_tracks


if __name__ == '__main__':
    app.run()
