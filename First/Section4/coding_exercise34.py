# The following paths are given:

# path1 = 'youtube.com/watch?v=5EhRztVxums'
# path2 = 'google.com/search?q=car'

# Using the appropriate method check if the paths refer to YouTube (e.g. start with 'youtube'). Print the result to the console as shown below.

# Expected result:

# path1: True
# path2: False

path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

check_p1 = "youtube.com" in path1
check_p2 = "youtube.com" in path2

print(f"path1: {check_p1}")
print(f"path2: {check_p2}")