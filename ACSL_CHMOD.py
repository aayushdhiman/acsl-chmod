def oct2bin(p):
    if p == '0':
        return '000'
    elif p == '1':
        return '001'
    elif p == '2':
        return '010'
    elif p == '3':
        return '011'
    elif p == '4':
        return '100'
    elif p == '5':
        return '101'
    elif p == '6':
        return '110'
    elif p == '7':
        return '111'

def Permissions(v):
    if v == '0':
        return '---'
    elif v == '1':
        return '--x'
    elif v == '2':
        return '-w-'
    elif v == '3':
        return '-wx'
    elif v == '4':
        return 'r--'
    elif v == '5':
        return 'r-x'
    elif v == '6':
        return 'rw-'
    elif v == '7':
        return 'rwx'


a, b, c = input("Enter three numbers here:").split(",")
d, e, f = input("Enter three numbers here:").split(",")
g, h, i = input("Enter three numbers here:").split(",")
j, k, l = input("Enter three numbers here:").split(",")
m, n, o = input("Enter three numbers here:").split(",")

print((str(oct2bin(a))) + ' ' + (str(oct2bin(b))) + ' ' + (str(oct2bin(c))) + ' ' + 'and' + ' ' + Permissions(a) + ' '
      + Permissions(b) + ' ' + Permissions(c))
print((str(oct2bin(d))) + ' ' + (str(oct2bin(e))) + ' ' + (str(oct2bin(f))) + ' ' + 'and' + ' ' + Permissions(d) + ' '
      + Permissions(e) + ' ' + Permissions(f))
print((str(oct2bin(g))) + ' ' + (str(oct2bin(h))) + ' ' + (str(oct2bin(i))) + ' ' + 'and' + ' ' + Permissions(g) + ' '
      + Permissions(h) + ' ' + Permissions(i))
print((str(oct2bin(j))) + ' ' + (str(oct2bin(k))) + ' ' + (str(oct2bin(l))) + ' ' + 'and' + ' ' + Permissions(j) + ' '
      + Permissions(k) + ' ' + Permissions(l))
print((str(oct2bin(m))) + ' ' + (str(oct2bin(n))) + ' ' + (str(oct2bin(o))) + ' ' + 'and' + ' ' + Permissions(m) + ' '
      + Permissions(n) + ' ' + Permissions(o))