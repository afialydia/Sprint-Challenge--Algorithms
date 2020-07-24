'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # possibly the base case? we need to only get words that are at least 2 characters because anything less wouldn't return "th"


    # i am going to review the first two characters of the string at a time using range options. 0 is implied? but I'll put it there anyway for posterity and renforcement. 2 stops before the 3rd ([2]) index. I'm checking to see if the first two characters of the string are "th"


    # so then I'll need a statement for if "th" is present in the word. if it is we will add one to the count and recurse again starting one index deeper into the word? .

    # my else should do the same as my elif but not include the count.

    
    pass


print(count_th('tabathathatha'))