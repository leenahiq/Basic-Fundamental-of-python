fav_songs = ["chandlier","believer","let me love you"]
print(fav_songs)

#access item in list by index usin []

print(fav_songs[2])
#how to update any item by index
fav_songs[-1] = "thunder"
print(fav_songs)

#finding the length of list usin len

print(len(fav_songs))

#add item at the end of the list use .append method
fav_songs.append("gangster")
print(fav_songs)

#to delete last item of the list

fav_songs.pop()
print(fav_songs)


fav_series_on_netflix = ["witcher","ghotam","titans"]
print(fav_series_on_netflix )

fav_series_on_netflix.append("reign")
fav_series_on_netflix.append("the order")
print(fav_series_on_netflix )
fav_series_on_netflix = ["witcher","ghotam","titans"]
print(fav_series_on_netflix )

fav_series_on_netflix.append("reign")
fav_series_on_netflix.append("the order")

fav_series_on_netflix.pop()
print(fav_series_on_netflix)
#activity 2

#remove.pop use to remove any item from list it only takes one perameter
fav_series_on_netflix.remove("reign")
print(fav_series_on_netflix)

#.reverse()reverse the list order
fav_series_on_netflix.reverse()
print(fav_series_on_netflix)

#.sort will sort out list alphabatically order from first letter
fav_series_on_netflix.sort()
print(fav_series_on_netflix)

#.count count number of item appers in list take one perameter

x = fav_series_on_netflix.count("titans")
print(x)

# .extend() merge two list together

fruits = ["apple","banana","cherry"]
veg = ["onion","cucumber","tomatoes"]
fruits.extend(veg)
print(fruits)


