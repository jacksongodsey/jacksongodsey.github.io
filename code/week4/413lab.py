phone_number = int(input())

area_code = phone_number // 10000000
middle_three = (phone_number // 10000) % 1000
final_four = phone_number % 10000
print(f'({area_code}) {middle_three}-{final_four}')
