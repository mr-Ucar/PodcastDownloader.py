# mr-Ucar
# Version 2.0

## USAGE TIP: Find a Podcast website, find the Audio Podcast
# and Right Click with the mouse and Copy the Podcast URL and Paste it when the scripts asks for it.

# EXAMPLE: https://www.bbc.co.uk/learningenglish/english/course/how-to-speak-english/unit-1/session-1
# Then give a name for the podcast
# and the script will download the podcast for you and show the local path of the downloaded file.

import requests
import re
from tqdm import tqdm
import os
from time import sleep
import re


sleep(0.1)

print("\n\n")


def print_banner():
    print("·.¸¸.·♩♪♫ Podcast Downloader by mr-Ucar ♫♪♩·.¸¸.·")


print_banner()

sleep(0.1)
print(
    "\n\nThis simple Python code will download an mp3 podcast when you provide the download link.\n"
)

sleep(0.1)
# Example Podcast Links - Check the URLS, sometiems it may not work, THE URL's can be changed.
print("\n\tExample Podcast Links to give an idea: \n")
sleep(0.5)
print("Check these links and find the Audio link(mp3 file) to download.")
sleep(0.2)
print("- BBC Learning Podcasts: https://www.bbc.co.uk/programmes/p0hc2grp")
sleep(0.1)
print(
    "- British Council Podcasts: https://learnenglish.britishcouncil.org/general-english/audio-series/podcasts"
)
sleep(0.1)
print("- VOA Learning English podcasts: https://learningenglish.voanews.com/podcasts")
sleep(0.1)
print("- NPR Podcasts: https://www.npr.org/podcasts/")
sleep(0.1)
print("- TED Talks: https://www.ted.com/podcasts")
sleep(0.1)
print("- The Guardian Podcasts: https://www.theguardian.com/podcasts")
sleep(0.1)
print("- The New York Times Podcasts: https://www.nytimes.com/column/the-daily")
sleep(0.1)
print("- The Washington Post Podcasts: https://www.washingtonpost.com/podcasts/")
sleep(0.1)
print("- The Wall Street Journal Podcasts: https://www.wsj.com/podcasts")
sleep(0.1)
print("- The Economist Podcasts: https://www.economist.com/podcasts")
sleep(0.1)
print("- The Financial Times Podcasts: https://www.ft.com/podcasts")
sleep(0.1)
print("- The Atlantic Podcasts: https://www.theatlantic.com/podcasts/")
sleep(0.1)
print("- The New Yorker Podcasts: https://www.newyorker.com/podcasts")
sleep(0.2)
print(" \nEXAMPLE AUDO LINK:  https://www.bbc.co.uk/programmes/p0h6ffwg")
sleep(0.5)
print("\nJust find the Audio File on the page and paste the link here.")
sleep(0.5)
print("")


print("\n\tPlease paste the URL of the Audio podcast/mp3 file, not a Video link")
sleep(0.5)
url = input("\tPaste the URL of the podcast/mp3 file:   ")
sleep(0.1)

# Validate the URL input
pattern = r"^https?://.*\.(mp3|wav|ogg|aac|flac|wma|m4a)$"
if not re.match(pattern, url):
    print("\nInvalid URL. Please provide a valid audio file URL.\n")
    sleep(0.1)
    print("The URL should end with .mp3 or ensure it is an audio file URL.")
    sleep(0.1)
    print("Try next time...Exiting...\n")
    sleep(0.1)
    exit()

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Get the name of the podcast
    nameofthePodcast = input(
        "Give the name of the podcast. So I can rename the downloaded file:  "
    )

    # Download the podcast with a progress bar
    total_size_in_bytes = int(response.headers.get("content-length", 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
    with open(f"{nameofthePodcast}.mp3", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            file.write(chunk)
    progress_bar.close()

    # Get the absolute path of the downloaded file
    downloaded_file_path = os.path.abspath(f"{nameofthePodcast}.mp3")

    print(f"\nThe podcast/audio file - {nameofthePodcast} - has been downloaded.")
    print(f"The file is located at: {downloaded_file_path}")
except requests.RequestException as e:
    print(f"Failed to download podcast: {e}")
sleep(0.1)
print("\n\tExited")
