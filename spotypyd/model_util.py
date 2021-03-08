import time


def model_track_data(tracks: list) -> dict:
    modelled_tracks = {"tracks": []}

    for i in tracks:
        track = i["track"]
        url = track["external_urls"]["spotify"]

        artist_names = []
        for artists in track["artists"]:
            artist_names.append(artists["name"])

        track_title = track["name"]
        artist_names = ", ".join(artist_names)
        date = convert_date(track["album"]["release_date"])
        image = track["album"]["images"][0]["url"]

        seconds = int(track["duration_ms"] / 1000)
        duration = time.strftime("%M:%S", time.gmtime(seconds))

        track_title = track_title.split("(", 1)[0]
        track_title = track_title.split("-", 1)[0]

        modelled_tracks["tracks"].append({
            "music_url": url,
            "artist": "by " + artist_names,
            "track_title": track_title,
            "album_image": image,
            "duration": duration,
            "release_date": date
        })

    return modelled_tracks


def convert_date(date):
    month = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }
    date = date.split("-")
    date = month.get(date[1]) + " " + date[2] + ", " + date[0]

    return date
