from pprint import pprint
import requests
key = 'AIzaSyDydO7b7FiI_S5fEvXwbu2miCe1POz6oPk'
# string interpolation
search = input("검색어를 입력해 주세요 : ")
q = f'q={search}'
my_type = f'type=video'
part = 'part=snippet'
maxResults = 'maxResults=20'
order = 'order=date'

url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{maxResults}&{order}&{q}'
print(url)
# 1. 검색어를 입력하면
# 2. 영상들을 검색할 것
# 3. 그 영상들의 제목과 채널명 출력

response = requests.get(url)
data = response.json()
pprint(data)
# ***********채널명, 영상 제목 출력하기***********
for data in data['items'][:10] :
    print(data['snippet']['title'], end=' :::::::::: ')
    print(data['snippet']['channelTitle'])
