import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "ce33ad0c5924f208613fab9ffef70535"

    def getPopulars(self, page):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()
    def nowPlaying(self, page):
        response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()
    def getSearchResult(self, keyword, page):
        response = requests.get(f"{self.api_url}/search/movie?api_key={self.api_key}&query={keyword}&page={page}")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1. Popular Movies\n2. Now Playing\n3. Search\n4. Exit\nSeçim: ")

    if secim == '4':
        print('Çıkış yaptınız.')
        break
    else:
        if secim == '1':
            page = int(input('Kaçıncı sayfayı açmak istiyorsunuz: '))
            movies = movieApi.getPopulars(page)
            for movie in movies['results']:
                print(f"Filmin adı: {movie['title']}\nYayınlanma tarihi: {movie['release_date'][:4]}\nAldığı puan: {movie['vote_average']}\n")
        if secim == '2':
            page = int(input('Kaçıncı sayfayı açmak istiyorsunuz: '))
            movies = movieApi.nowPlaying(page)
            for movie in movies['results']:
                print(f"Filmin adı: {movie['title']}\nYayınlanma tarihi: {movie['release_date'][:4]}\nAldığı puan: {movie['vote_average']}\n")
        if secim == '3':
            keyword = input('Aramak istediğiniz filmin adını girin.: ')
            page = int(input('Kaçıncı sayfayı açmak istiyorsunuz: '))
            movies = movieApi.getSearchResult(keyword, page)
            for movie in movies['results']:
                print(f"Filmin adı: {movie['title']}\nYayınlanma tarihi: {movie['release_date'][:4]}\nAldığı puan: {movie['vote_average']}\n")