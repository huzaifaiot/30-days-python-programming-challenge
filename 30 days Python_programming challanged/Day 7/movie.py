def main():
    favorite_movies = []

    while True:
        movie = input("Enter your favorite movie (type 'stop' to end): ")
        if movie.lower() == 'stop':
            break
        else:
            favorite_movies.append(movie)

    print("\nYour favorite movies:")
    for movie in favorite_movies:
        print(movie)

if __name__ == "__main__":
    main()
