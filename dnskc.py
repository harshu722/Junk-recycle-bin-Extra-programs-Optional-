import imdb  
  
# creating instance of IMDb  
movie_obj = imdb.IMDb()  
  
# movie name  
name = "Pushpa"  
  
# searching the movie  
search = movie_obj .search_movie(name)  
  
# printing the result  
for i in search:  
    print(i)
