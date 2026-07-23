from util.exercise_output import print_exercise_header


def make_album(artist_name: str, album_title: str, track_count=None):
    return {"artist": artist_name, "title": album_title, "track_count": track_count}


print_exercise_header("8-7 Album")

first_album = make_album("Pink Floyd", "Animals")
second_album = make_album("Rush", "Moving Pictures")
third_album = make_album("Nirvana", "Nevermind", 10)

print(first_album)
print(second_album)
print(third_album)
