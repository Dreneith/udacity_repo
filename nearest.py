from tokenize import Name


def nearest_square(num):
    '''
    It returns nearest perfect square that is less or equal to num
    Args:
        num: it accepts an integer only
    '''
    #Try to return the nearest square but if not int
    try:
        root = 0
        while (root + 1) ** 2 <= num:
            root +=1
        return root ** 2
    except (SyntaxError, NameError, TypeError,ValueError):
        print("Please put in a real number")
    

if __name__ == "__main__":
    print (nearest_square('we'))