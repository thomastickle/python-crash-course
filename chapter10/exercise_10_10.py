from collections import Counter
import re

from util.exercise_output import print_exercise_header

from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


MOBY_DICK_URL = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
SAVE_FILE = OUTPUT_DIR / "exercise_10_10.txt"


def download_moby_dick() -> Path | None:
    """Download Moby-Dick unless it already exists."""

    destination = SAVE_FILE
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        print(f"{destination.name} already exists. Skipping download.")
        return destination

    request = Request(
        MOBY_DICK_URL,
        headers={"User-Agent": "Python learning exercise"},
    )

    try:
        with urlopen(request, timeout=30) as response:
            destination.write_bytes(response.read())
    except (HTTPError, URLError, TimeoutError) as error:
        print(f"Could not download Moby-Dick: {error}")
        return None

    print(f"Moby-Dick downloaded to {destination}.")
    return destination


def count_words(file_path: Path) -> int:
    contents = file_path.read_text().casefold()
    all_words = re.findall(r"[a-z]+", contents)
    word_counts = Counter(all_words)
    return word_counts["the"]


print_exercise_header("10-10")

downloaded_file = download_moby_dick()
if downloaded_file is not None:
    count = count_words(downloaded_file)
    print(f"Count of 'the' was {count}")
