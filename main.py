
# ex 1
def find_index(element, l):
    """:parameter: element, list
        Find on which position in the list is the element
        If there is no element in the list :return: ‘None’"""
    n = 0
    for ele in l:
        if ele == element: #if you want to compare you use ==
            print(n)
        n = n + 1

find_index(9, [8,3,5,9])

#ex 1.5

def find_index2(element, l):
    """:parameter: element, list
        Find on which position in the list is the element
        If there is no element in the list :return: ‘-1’"""
    n = 0
    for ele in l:
        if ele == element: #if you want to compare you use ==
            return(n)
        n = n + 1
    return(-1)

print(find_index2(0, [9,8,3,56]))

def find_value(element, d):
    """:parameter: element, dict
        :return: the value corresponding to the element
        If the element is not in dict :return: ‘None’"""

    for stops in d.keys():
        if stops == element:
            return(d[stops])

train_stops = {'hengelo': 1, 'almelo': 2, 'deventer': 3, 'apeldoorn': 4}
print(find_value('deventer', train_stops))

# ex 2.
def firt_five(l):
    """:parameter:: list
        ::return:: a tuple of first five elements of the list"""
    N=5
    return(l[:N])

trip_to_rotterdam = ['amersfoort', 'utrecht', 'gouda', 'alexander', 'voorschoterlaan', 'vredehofweg']
tuple1 = tuple(trip_to_rotterdam)
print(firt_five(tuple1))

def first_five_to_tuple(l):
    """:parameter:: list
    ::return:: a list of first five elements"""
    N = 5
    return (l[:N])
i_am_in_rotterdam = ['parties', 'music', 'food', 'buildings', 'friends', 'new people', 'mocktails']
print(first_five_to_tuple(i_am_in_rotterdam))

def reverse_list(l):
    """:parameter:: list
        ::return:: reverse the list"""
    return (list(reversed(l)))

spendings_in_rotterdam = [2.50, 2.30, 5.27, 0.70]
print(reverse_list(spendings_in_rotterdam))

def convert(s):
    """::parameter:: string
        ::return:: turn the string into tuple of letters in the word"""
    return tuple(list(s))
    #probably incorrect cause i used list but i am not sure

string1 = 'counterclockwise'
print(convert(string1))

def convert_on_space(s):
    """::parameter:: string
        ::return:: turn the string into tuple of word in the word
        example:   convert_on_space("Hey, it is Pola here!")
        returns ("Hey,", "it", "is", "Pola", "here!")
        """
    return(tuple(s.split()))

print(convert_on_space("Hey Pola, nice to meet you!"))