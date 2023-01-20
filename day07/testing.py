str = ['h','e','l','o'];

strLen = len(str) - 1;
n = 0;

while n <= strLen:
    temp = str[strLen-n];
    print(temp);
    str[strLen-n] = str[n];
    print(str[strLen-n]);
    str[n] = temp;
    
    n += 1;

print(str);