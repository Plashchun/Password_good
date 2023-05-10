password = input('Enter your password: ')

recommendation = ''
score = 0
l_isupper = False
l_islower = False
l_digit = False
l_spec = False

if len(password) >= 8:
    score += 1
else:
    recommendation += 'The min password length is 8\n'

for char in password:
    if char.isupper():
        l_isupper = True
    if char.islower():
        l_islower = True
    if char.isdigit():
        l_digit = True
    if not char.isdigit() and not char.isalpha():
        l_spec = True

score += l_isupper + l_islower + l_digit + l_spec

if not l_isupper:
    recommendation += 'Use capital letters\n'
if not l_islower:
    recommendation += 'Use lower letters\n'
if not l_digit:
    recommendation += 'Use digits\n'
if not l_spec:
    recommendation += 'Use special characters\n'

print(f'Password score: {score}')
if recommendation:
    print('Recommendation:')
    print(recommendation)