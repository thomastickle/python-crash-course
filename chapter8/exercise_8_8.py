from util.exercise_output import print_exercise_header


def make_album(artist_name: str, album_title: str, track_count=None):
    return {"artist": artist_name, "title": album_title, "track_count": track_count}


print_exercise_header("8-7 Album")


while True:
    artist_name = input("Please input artist name: ")
    if artist_name == "quit":
        break

    album_title = input("Please input album title: ")
    if album_title == "quit":
        break

    print(make_album(artist_name, album_title))
