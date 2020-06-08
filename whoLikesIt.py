def likes(names):
    whoLikes = ''

    if (len(names) == 0):
        whoLikes = 'no one likes this'
    elif (len(names) == 1):
        whoLikes = str(names[0]) + ' likes this'
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            whoLikes += names[name] + ', '
        whoLikes = whoLikes[:-2]
        whoLikes += ' and ' + str(names[len(names) - 1]) + ' like this'
    else:
        for name in range(0, 2):
            whoLikes += names[name] + ', '
        whoLikes = whoLikes[:-2]
        whoLikes += ' and ' + str(len(names)-2) + ' others like this'
    return whoLikes