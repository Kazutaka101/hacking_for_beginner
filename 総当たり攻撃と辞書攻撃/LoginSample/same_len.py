msg1 = "login ok"
msg2 = "login no"

msg1_ascii_sam = 0
msg2_ascii_sam = 0

for char in msg1:
    msg1_ascii_sam += ord(char)

for char in msg2:
    msg2_ascii_sam += ord(char)
print(f'msg1_len:{len(msg1)}')
print(f'msg2_len:{len(msg2)}')
       
print("")
print(f'msg1_ascii_sam:{msg1_ascii_sam}') 
print(f'msg2_ascii_sam:{msg2_ascii_sam}')
