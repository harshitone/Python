#  Ask the user for their 3 favorite movies and store them in a list.

Movie1 = input("Enter your first favourite movie :")
Movie2 = input("Enter your Second favourite movie :")
Movie3 = input("Enter your third favourite movie :")

#method1

# listMovie = [Movie1,Movie2,Movie3]
# print(listMovie)

#Method2

movieList = []
movieList.append(Movie1)
movieList.append(Movie2)
movieList.append(Movie3)
print(movieList)