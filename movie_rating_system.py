
movies = {}
def add_movie():
    name = input("Enter movie name: ")
    if name in movies:
        print("Movie already exists.")
    else:
        movies[name] = []
        print("Movie added successfully.")

def rate_movie():
    name = input("Enter movie name to rate: ")
    if name in movies:
        rating = float(input("Enter rating (1-5): "))
        if 1 <= rating <= 5:
            movies[name].append(rating)
            print("Rating added.")
        else:
            print("Rating must be between 1 and 5.")
    else:
        print("Movie not found.")

def display_movies():
    if not movies:
        print("No movies available.")
    else:
        for movie, ratings in movies.items():
            if ratings:
                avg = sum(ratings) / len(ratings)
                print(f"{movie} -> Ratings: {ratings} | Average: {avg:.2f}")
            else:
                print(f"{movie} -> No ratings yet")

def search_movie():
    name = input("Enter movie name to search: ")
    if name in movies:
        print("Movie found:", name)
        print("Ratings:", movies[name])
    else:
        print("Movie not found.")

while True:
    print("\n--- Movie Rating System ---")
    print("1. Add Movie")
    print("2. Rate Movie")
    print("3. Display Movies")
    print("4. Search Movie")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        rate_movie()
    elif choice == "3":
        display_movies()
    elif choice == "4":
        search_movie()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
