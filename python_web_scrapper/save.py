import csv

def save_to_file(movies):
    file = open("C:/Users/pixels-99/Desktop/jobs/movies.csv", mode="w", newline="")
    writer = csv.writer(file)
    writer.writerow(["rank","movie_name","picture"])
    for movie in movies:
        writer.writerow(list(movie.values()))
    return