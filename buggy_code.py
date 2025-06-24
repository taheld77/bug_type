def average_lists(list1, list2):
    sum = 0
    for number in list2:
        list1.append(number)
    for number in list1:
        sum += number
    average = sum / len(list1)
    print(f"the average is: {average}")

def main():
    average_lists([60, 30], [30, 20])

if __name__ == '__main__':
        main()