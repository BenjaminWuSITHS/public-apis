import json

with open("jikan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

anime_list = data["data"]   # a list of 25 anime (each one is a dictionary)


# ------------------------------------------------------------
# Q1. Filtering and counting
# Print the title and score of every anime with a score
# greater than 9.0. Then print how many there were.
# ------------------------------------------------------------

for anime in anime_list:
    if anime['score'] > 9.0:
        print(anime['title'])


# ------------------------------------------------------------
# Q2. Accumulator
# Calculate and print the average score of all the anime
# in the list. Round the answer to 2 decimal places.
# ------------------------------------------------------------

final =0
for anime in anime_list:
    final += anime['score']
print(round(final/len(anime_list),2))


# ------------------------------------------------------------
# Q3. Finding the maximum
# Print the title and episode count of the anime that has the
# most episodes.
# Hint: look closely at the "episodes" values. Does every
# anime have a number?
# ------------------------------------------------------------
lists=[]

for i in anime_list:
    if i['episodes'] != None:
        lists.append(i['episodes'])
for i in anime_list:
    if max(lists) == i['episodes']:
        print(max(lists), i["title"])



# ------------------------------------------------------------
# Q4. Nested lists
# Each anime has a "genres" list. Each item in that list is a
# dictionary with a "name" key (for example, "Comedy").
# Print the title of every anime that has the genre "Comedy".
# ------------------------------------------------------------

for i in anime_list:
    for b in range(len(i['genres'])):
        if i['genres'][b]['name'] == "Comedy":
            print(i['title']) 


users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]

for user in users:
    if "role" in user:
        if user['role'] == 'admin':
            print(user['name'])

# or

for user in users:
    try:
        if user['role'] == 'admin':
            print(user['name'])
    except KeyError:
        continue