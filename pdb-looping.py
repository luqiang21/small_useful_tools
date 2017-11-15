# import pdb
#
# num_list = [500, 600, 700]
# alpha_list = ['x', 'y', 'z']
#
#
# def nested_loop():
#     for number in num_list:
#         print(number)
#         pdb.set_trace()
#         for letter in alpha_list:
#             print(letter)
#
# if __name__ == '__main__':
#     nested_loop()

# above are for looping.py

# below for sammy.py
def print_sammy():
    sammy_list = []
    sammy = 'sammy'
    for letter in sammy:
        sammy_list.append(letter)
        print(sammy_list)

if __name__ == "__main__":
    print_sammy()
