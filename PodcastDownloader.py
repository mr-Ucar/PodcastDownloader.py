
# mr-Ucar2023
# Example Podcast Site to improve English: https://www.bbc.co.uk/programmes/p02pc9tn/episodes/downloads

# Example BBC Learning Podcast to download: https://open.live.bbc.co.uk/mediaselector/6/redir/version/2.0/mediaset/audio-nondrm-download/proto/https/vpid/p0g4sl3m.mp3

import requests

print("\n\nThis simple Python code will download a mp3 podcast when you provide the download link\n")
url = input("\tPaste the URL of the podcast/mp3 file:  ")
print("")


r = requests.get(url)

content = r.content

nameofthePodcast = input("Give the name of the podcast. So I can rename the downloaded file:  ")

with open(f"{nameofthePodcast}.mp3","wb") as file:
    file.write(content)

print(f"\nThe podcast/audio file  - {nameofthePodcast} - has been downloaded.")

print("\n\tExitted")

