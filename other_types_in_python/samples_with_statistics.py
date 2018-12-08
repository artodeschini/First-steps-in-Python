import statistics

marks = [1, 6, 9, 23, 2]

# mean is 'media'in portuguese
m = statistics.mean(marks)
print(m)
# print(type(m))

# median is a 'mediana' in portuguese
m = statistics.median(marks)
print(m)
# print(type(m))

marks.append(7)

m = statistics.median(marks)
print(m)

low = statistics.median_high(marks)
print(low)

high = statistics.median_high(marks)
print(high)

var = statistics.variance(marks)
print(var)