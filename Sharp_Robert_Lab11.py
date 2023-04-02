#Sharp, Robert I used the videos and skype video as reference as well. Any places where pg isn't described was from videos
#Creating list pg 343-346
movie_list = []
#Keep going loop using the while loop
keep_going = 'y'
while keep_going == 'y':
    user_movie = input('Enter a movie:')
#End of loop using -1
    if user_movie == '-1':
        keep_going = 'n'
#else adding to the list pg.356
    else:
        movie_list.append(user_movie)
#Printing the movie names
print('The elements in the list include: ', end='')
#using for loop to create the list without [] and with a , between each except the end
for movie_index in range(0, len(movie_list)):
    movie_name = movie_list[movie_index]
    if movie_index == len(movie_list) - 1:
        print(movie_name,  end=' ')
    else:
        print(movie_name, end=', ')
#Repeting step 2 wity control+c and control+v
print('\nLength of the list', len(movie_list), end='')
print('\nDeleting index 0... ')
#using pop to delete space 0 input
movie_list.pop(0)
print('The elements in the list include: ', end='')
for movie_index in range(0, len(movie_list)):
    movie_name = movie_list[movie_index]
    if movie_index == len(movie_list) - 1:
        print(movie_name,  end=' ')
    else:
        print(movie_name, end=', ')

print('\nLength of the list', len(movie_list), end='')
