number = int(input('숫자를 입력하세요: '))

# fizz buzz => 3의 배수(3n) fizz / 5n buzz / 15 fizzbuzz

# 15 부터
# if number % 15 == 0:
#     print('fizzbuzz')
# elif number % 5 == 0:
#     print('buzz')
# elif number % 3 == 0:
#     print('fizz')
# else:
#     pass

# 3배수 먼저 걸릴 때
for i in range(1, number + 1):
    if i % 3 == 0:
        if i % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

# 15 부터 할 때
for i in range(1, number + 1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)


# and 사용
# if number % 3 == 0 and number % 5 == 0:
#     print('fizzbuzz')
# elif number % 3 == 0:
#     print('fizz')
# elif number % 5 == 0:
#     print('buzz')

# 1 ~ number 까지 출력
# 그와중에 3 fizz / 5 buzz / 15 fizzbuzz
# ex) 1 2 fizz 4 buzz ..

