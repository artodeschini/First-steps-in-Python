def calculate_simple_interest(principal, interest, duration) :
    total_interest = interest * 0.01 * duration * principal;
    return total_interest + principal


print( calculate_simple_interest(10000,5,5) )