__author__ = 'mnowotka'

from itertools import product
from string import ascii_uppercase

#-----------------------------------------------------------------------------------------------------------------------

t26 = [ t for t in map(''.join, product(ascii_uppercase, repeat=3)) if t[0]!='E' and (t < 'TAA' or t > 'TTV')]
d26 = map(''.join, product(ascii_uppercase, repeat=2))

#-----------------------------------------------------------------------------------------------------------------------

def base26_triplet_1(a):
    b0 = ord(a[0])
    b1 = ord(a[1]) & 0x3f
    h = b0 | b1 << 8
    return t26[h]

#-----------------------------------------------------------------------------------------------------------------------

def base26_triplet_2(a):
    b0 = ord(a[1]) & 0xc0
    b1 = ord(a[2])
    b2 = ord(a[3]) & 0x0f
    h =  (b0 | b1 << 8 | b2 << 16) >> 6
    return t26[h]

#-----------------------------------------------------------------------------------------------------------------------

def base26_triplet_3(a):
    b0 = ord(a[3]) & 0xf0
    b1 = ord(a[4])
    b2 = ord(a[5]) & 0x03
    h =  (b0 | b1 << 8  | b2 << 16) >> 4
    return t26[h]

#-----------------------------------------------------------------------------------------------------------------------

def base26_triplet_4(a):
    b0 = ord(a[5]) & 0xfc
    b1 = ord(a[6])
    h =  (b0 | b1 << 8) >> 2
    return t26[h]

#-----------------------------------------------------------------------------------------------------------------------

def base26_dublet_for_bits_28_to_36(a):
    b0 = ord(a[3]) & 0xf0
    b1 = ord(a[4]) & 0x1f
    h =  (b0 | b1 << 8) >> 4
    return d26[h]

#-----------------------------------------------------------------------------------------------------------------------

def base26_dublet_for_bits_56_to_64(a):
    b0 = ord(a[7])
    b1 = ord(a[8]) & 0x01
    h =  b0 | b1 << 8
    return d26[h]

#-----------------------------------------------------------------------------------------------------------------------


