import pandas as pd
from youtubesearchpython import VideosSearch

# Load the CSV data
data = pd.read_csv("newimdb4.csv")

# Extract movie names
movie_names = data["Series_Title"].iloc[0:4]

# Initialize an empty list to store video URLs
video_urls = []

# Search YouTube for each movie trailer and get the first video URL
for movie_name in movie_names:
    videosSearch = VideosSearch(movie_name + " trailer", limit=1)
    result = videosSearch.result()

    if len(result['result']) > 0:
        first_video_url = result['result'][0]['link']
        video_urls.append(first_video_url)
        print(f"Url has added for:{movie_name}")
    else:
        print(f"Trailer couldn't found for:{movie_name}")

# Extract video IDs from the URLs
video_ids = [url.split('=')[-1] for url in video_urls]

# Ensure the number of video IDs matches the number of rows in the DataFrame
num_rows = min(len(video_ids), len(data))

# Replace the 'trailer_url' column with the new video IDs
data['trailer_url'][:num_rows] = video_ids[:num_rows]

print(data["trailer_url"])
print(video_urls)
# Save the updated DataFrame to a new CSV file
data.to_csv( "new_file_name", index=False)
