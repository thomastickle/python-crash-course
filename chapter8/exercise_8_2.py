from util.exercise_output import print_exercise_header


print_exercise_header("8-2 Favorite Book")


def favorite_book(book_title: str):
    print(f"One of my favorite books is {book_title.title()}.")


favorite_book("The Two Towers")
