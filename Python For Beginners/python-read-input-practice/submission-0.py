def add_two_numbers() -> int:
    sum = 0
    user_input = input().split(",")
    for i in range(len(user_input)):
        sum += int(user_input[i])
    return sum




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
