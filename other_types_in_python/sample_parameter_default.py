def sample_of_a_method(mandatory, default_parameter='Default', *args, **kwargs):
    print(f'mandatory {mandatory} default_parameter {default_parameter} args {args} kwargs {kwargs}')


sample_of_a_method('teste')
sample_of_a_method('another', 'try')

sample_of_a_method('mandatory', 'string1', 'string2', 'string3', 'string4', 'string5')
sample_of_a_method(mandatory='mandatory')

sample_of_a_method('mandatory', 'string1', 'string2', 'string3', 'string4', key1='1', key2='2')

same_list = [1, 2, 3, 4, 5, 7]

sample_of_a_method(*same_list)

same_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

sample_of_a_method(*same_list, **same_dict)