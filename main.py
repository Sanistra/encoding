import random
def is_prime(P):
    n = random.randint(1, P)
    if n < 2:
        return is_prime(P)
    if n == 2:
        return n
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return is_prime(P)
    return n
def gcd(a, b):
    arr = [[a, 0, 0], [b, 1, a // b], [a % b]]
    while(arr[len(arr)-1][0] != 0):
        arr[len(arr) - 1].append(arr[len(arr)-3][1] - (arr[len(arr)-2][1] * arr[len(arr)-2][2]))
        arr[len(arr) - 1].append(arr[len(arr)-2][0] // arr[len(arr)-1][0])
        arr.append([arr[len(arr)-2][0] % arr[len(arr)-1][0]])
    return ((arr[len(arr)-2][1] + a) % a)
def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


alp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ,.'
f = open('input.txt', 'r')
message = str(f.read())
f.close()
print('message is:', message)
secret = ''
P = 87641
for i in range(len(message)):
    secret += str(alp.find(message[i]) + 10)#преобразовали строку
secret = (list(secret))

pieces = []
pieces.append(0)
buf = ''
for i in range(len(secret)):
    buf += secret[i]
    if (int(buf) < P):
        pieces[len(pieces)-1] = int(buf)
    else:
        buf = secret[i]
        pieces.append(0)
print('pieces:', pieces)
f = open('output.txt', 'w')
f.write('Message is:')
f.write(message)
f.write('\n')
res_text = ''
for i in range(len(pieces)):
    x = []
    f.write('sipherpiece')
    f.write(str(i+1))
    f.write(':')
    ca = is_prime(P)
    da = gcd(P - 1, ca)
    cb = is_prime(P)
    db = gcd(P - 1, cb)
    x.append(pieces[i])
    f.write(str(x[len(x)-1]))
    x.append((fast_pow(x[len(x)-1], ca)) % P)
    f.write(str(x[len(x)-1]))
    x.append(fast_pow(x[len(x)-1], cb) % P)
    f.write(str(x[len(x)-1]))
    x.append(fast_pow(x[len(x)-1], da) % P)
    f.write(str(x[len(x)-1]))
    x.append(fast_pow(x[len(x)-1], db) % P)
    f.write(str(x[len(x)-1]))
    res_text += str(x[len(x)-1])
    f.write('\n')
    print('piece', i+1, ':', x)

#print(res_text)
decrypt_text = ''
for i in range(0, len(res_text), 2):
    decrypt_text += alp[int(res_text[i] + res_text[i + 1]) - 10]
print(decrypt_text)
f.write('decrypt_text:')
f.write(decrypt_text)
f.close()