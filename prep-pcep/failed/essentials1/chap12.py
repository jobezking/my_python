'''
Logical operators: and, or,  not
Bitwise operators: & (and), | (or), ^ (not), ~ (xor)
'''

flag_register = 0x1234
the_mask = 0x8

flag_register = flag_register & ~the_mask
# alternatively
flag_register &= ~the_mask

# binary shift: integer operation only
to_shift  = 16
shift_right = to_shift >> 1
shift_left = to_shift << 2
print(to_shift, shift_right, shift_left)