from youtube_search import YoutubeSearch
import sys

base = "https://www.youtube.com/watch?v="
keyword = ' '.join(sys.argv[1:])
result = YoutubeSearch(keyword, max_results=1).to_dict()
url = base + result[0]['id']
print(url)