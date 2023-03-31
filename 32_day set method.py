s = {"Assam","Delhi","Bangaluru","Chennai"}
s2 = {"Assam","Chennai","Kolkata","Kerala"}

print(s.union(s2))              #merge two set
s.update(s2)                    #Update the set with another set, or any other iterable
print(s2)
# s.clear()    #remove all value from the set
# del s       delete the whole set
s.add("Mumbai")  #add an element to the set
print(s)
# s.discard("Assam")     #remove an element from the set without throwoing any error
print(s.pop())          #remove an random element and return it






 
        #    Table of Python Set Methods

# Functions Name	                       Description

# add()	                            Adds a given element to a set
# clear()	                        Removes all elements from the set
# copy()	                        Returns a shallow copy of the set
# difference()	                    Returns a set that is the difference between two sets
# difference_update()	            Updates the existing caller set with the difference between two sets
# discard()	                        Removes the element from the set
# frozenset()	                    Return an immutable frozenset object
# intersection()	                Returns a set that has the intersection of all sets
# intersection_update()	            Updates the existing caller set with the intersection of sets
# isdisjoint()	                    Checks whether the sets are disjoint or not
# issubset()	                    Returns True if all elements of a set A are present in another set B
# issuperset()	                    Returns True if all elements of a set A occupies set B
# pop()	                            Returns and removes a random element from the set
# remove()	                        Removes the element from the set
# symmetric_difference()	        Returns a set which is the symmetric difference between the two sets
# symmetric_difference_update()	    Updates the existing caller set with the symmetric difference of sets
# union()	                        Returns a set that has the union of all sets
# update()	                        Adds elements to the set