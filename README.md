# PlaylistAlgorythm
Given a list of songs ordered by desirability, a target length, and an acceptable variance, returns a list of those songs that have the given length within the given variance.  
If there is more than one list that satisfies the requirements, it will return the list with the most desireable songs

# Example
  music = [{'name': 'song1', 'length': '0:02'}, {'name': 'song2', 'length': '1: 53'}, {'name': 'song3', 'length': '3:23'}]

  print(create_playlist(music, 115, 0))  # ['song1', 'song2']  
  print(create_playlist(music, 113, 0))  # ['song2']  
  print(create_playlist(music, 318, 0))  # ['song1', 'song2', 'song3']  
  print(create_playlist(music, 318, 4))  # ['song1', 'song2', 'song3']  
  print(create_playlist(music, 318, 300))  # ['song1', 'song2']
  
# Core ideas
  The meat of the work is done by the numberAlgorythm class.  After converting the song lengths to base ten, we add them to a list one at a 
  time, and after we add each number to the list, we find the sum of it with each number currently in the list.  We add all of these 
  numbers to the list as well.  In this way, we maintain a list of all possible sums as we go.  Important to note, every time we consume 
  a new number, the new length of the list is equal to twice the length of the old list + 1.  Becuase of this, as soon as the target number
  shows up in the list of possible sums, we can use the position of that number to figure out exactly which songs were used to make up that
  number
  
# Future Work
  My goal is to modify it to be a user friendly program which first promts for the target number and variance, and then continually asks for songs until it can create a playlist matching the requirements
  I would also like to refactor the different bits into different files and make the tests more official
  Lastly, I would like to work on the Core Ideas section to make it make any sense

  
