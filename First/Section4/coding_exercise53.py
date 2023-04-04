# Tuples are immutable. The following tuple is given:

# members = (('Kate', 23), ('Tom', 19))

# Insert a tuple ('John', 26) between Kate and Tom as shown below. Print the result to the console.

# Tip: You have to create a new tuple.

# Expected result:

# (('Kate', 23), ('John', 26), ('Tom', 19)

members = (('Kate', 23), ('Tom', 19))
cv_lst =list(members)
cv_lst.insert(1,('John',26))
new_member = tuple(cv_lst)

print(new_member)