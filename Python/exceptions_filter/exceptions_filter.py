DAYS = ['Monday', 'Tuesday', 'Wednes\
    day', 'Thursday', 'Friday', 'Satu\
        rday', 'Sunday']


def find_in_list(index, myList):
    return myList(index)


def exceptions_light_filter(index, myList):
    try:
        return find_in_list(index, myList)
    except IndexError:
        return None
