import re

def hex_to_int(msg, current):
    temp16 = ''
    msg[current].reverse()
    for i in range(len(msg[current])):
        temp16 = temp16 + msg[current][i]
    temp16 = re.sub('0x', '', temp16)
    temp = int(temp16, 16)

    return temp

# input method
msg = input('Type charater: ')
msg_l = list(msg)
# msg to hex list
msg_h = []
for x in msg_l:
    msg_h.append(hex(ord(x)))

int_l = []
length = len(msg_h)
# split list /4
n = 4
msg_s = [msg_h[i * n:(i + 1) * n] for i in range((len(msg_h) - 1 + n) // n)]

for i in range((len(msg_h) - 1 + n) //n):
    int_l.append(hex_to_int(msg_s,i))
int_l.reverse()
print (int_l)
