# to create a list use []
squares_for_ten_first_numbers = [i*i for i in range(1,11)]
print(type(squares_for_ten_first_numbers))
print(squares_for_ten_first_numbers)

squares_for_ten_first_numbers_set = set( squares_for_ten_first_numbers )
print(type(squares_for_ten_first_numbers_set))
print(squares_for_ten_first_numbers_set)

# to create a set use {}
squares_for_ten_first_numbers_set_2 = {i*i for i in range(1,11)}
print(type(squares_for_ten_first_numbers_set_2))
print(squares_for_ten_first_numbers_set_2)

# to create with a dictionary
squares_for_ten_first_numbers_dict = {i: i*i for i in range(1,11)}
print(type(squares_for_ten_first_numbers_dict))
print(squares_for_ten_first_numbers_dict)

print(type([]))         # list
print(type({}))         # dict
print(type({1}))        # set
print(type(set({})))    # set
print(type({1: 1}))     # dict
print(type(()))         # tuple
