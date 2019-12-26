# 2019.01.01 ~ 현재까지의 소프트웨어 이슈제목과 링크를 받아오는 프로그램
from news import movie_rank as movie
from save import save_to_file as save

movies = movie()
save(movies)