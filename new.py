
# # 1
# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print(my_tuple[2:6])

# # 2
# print(5 in my_tuple) 
# print(11 in my_tuple)

# # 3
# try:
#     my_tuple[2] = 100  
# except TypeError as e:
#     print(e)

# # 4

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# union_set = set1.union(set2)
# print(union_set) 
# intersection_set = set1.intersection(set2)
# print(intersection_set) 
# set1.add(9)
# print(set1)
# set1.remove(2)
# print(set1) 



# ფილმების სია
# movielist = [
#     ("Doctor who", 2010, "Sci-Fi"),
#     ("Titanic", 1997, "Romance"),
#     ("The Dark Knight", 2008, "Action"),
#     ("Interstellar", 2014, "Sci-Fi"),
#     ("Forrest Gump", 1994, "Drama"),
#     ("The Matrix", 1999, "Sci-Fi"),
#     ("Gladiator", 2000, "Action"),
#     ("in the middle of the cithy",2010, "Comedy"),
# ]
# def get_movies_by_genre(movies, genre):
#     return [movie for movie in movies if movie[2].lower() == genre.lower()]


# user_genre = input("Enter a genre to search for: ")

# movies = get_movies_by_genre(movielist, user_genre)
# if movies:
#     print(f"Movies in the '{user_genre}' genre:")
#     for movie in movies:
#         print(movie)
# else:
#     print(f"No movies found in the '{user_genre}' genre.")






# user_input = input("Enter the text to add to the file: ")
# user_input2 = input("Enter date")
# with open("diari.txt", "a") as file_open:
#     file_open.write(user_input + '\n') 
#     file_open.write(user_input2 + '\n') 
# with open('diari.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

import csv
header = ["name", "subject_first", "subject_second"]
students = [
    ["Giorgi", "english", "math"],
    ["Mamuka", "History", "geography"],
    ["Sopho", "math", "french"],
    ["Davit", "Georgian", ""],
    ["Vano", "english", "History"],
]
with open("students.csv", "w") as f:
    csv.writer(f).writerow(header)
    csv.writer(f).writerows(students)
with open("students.csv", "a") as f:
    csv.DictWriter(f, fieldnames=header).writerow({"name": "Lasha", "subject_first": "english", "subject_second": "math"})
with open("students.csv", "r") as f:
    for row in csv.DictReader(f):
        print(f"Name: {row['name']}, Subject 1: {row['subject_first']}, Subject 2: {row['subject_second']}")