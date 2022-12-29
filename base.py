def dec_to_base(num,base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base

    base_num = base_num[::-1]
    print(base_num)
a=int(input())
b=int(input())
dec_to_base(a,b)
