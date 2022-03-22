binary_number = input()

binary_number_int = int(binary_number)

first_digit = binary_number_int // 1000
second_digit = binary_number_int // 100 % 10
third_digit = binary_number_int // 10 % 10
fourth_digit = binary_number_int % 10
final_output = (first_digit * (8)) + (second_digit * (4)) + (third_digit *
(2)) + (fourth_digit * (1))

print(final_output)
