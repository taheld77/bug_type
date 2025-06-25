def average_lists(list1, list2):
    """
    this function takes two lists and returns the average of them
    :param list1: list of numbers
    :param list2: list of numbers
    :return: average of list1 and list2
    """
    sum = 0
    list1.extend(list2)
    for number in list1:
        sum += number
    average = sum / len(list1)
    return average

def main():
    print(f"the average is: {average_lists([60, 30], [30, 20])}")

if __name__ == '__main__':
        main()