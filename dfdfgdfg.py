import requests

print(requests.post(f"http://localhost:8000/rec_genre_nonauth?genre=romantic"))
