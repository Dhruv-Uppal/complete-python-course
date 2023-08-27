# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie():
title = input("Enter the movie title: ")
director = input("Enter the movie director: ")
year = input("Enter the movie release year: ")

movies.append({
    'title': title,
    'director': director,
    'year': year
})

def show_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"title:{movie['Title']}")
    print(f"director:{movie['Director']}")
    print(f"year:{movie['year']}")

def find_movie():
    Search_Title=input("Enter the name of the movie you are looking for:")
    for movie in movies:
        if movie["title"]==Search_Title:
            print_movie(movie)

user_options={
    'a'=add_movie,
    'l'=show_movie,
    'f'=find_movie
}

# Create other functions for:
#   - listing movies
#   - finding movies


# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
        while selection != 'q':
            if selection == "a":
                pass
            elif selection == "l":
                pass
            elif selection == "f":
                pass
            else:
               print('Unknown command. Please try again.')

            selection = input(MENU_PROMPT)


menu()

# Remember to run the user menu function at the end!
