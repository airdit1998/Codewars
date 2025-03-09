# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing
# the names of people that like an item. It must
# return the display text as shown in the examples:
#

def likes(names):
    text_to_return = ""
    if len(names) == 0:
        text_to_return = "no one likes this"
    elif len(names) == 1:
        text_to_return = names[0] + " likes this"
    elif len(names) == 2:
        text_to_return = names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        text_to_return = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        text_to_return = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
    return text_to_return
