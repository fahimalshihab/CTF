
# ASCII and Regular expressions
```102 108 97 103 123 102 97 107 101 32 121 111 117 117 125 125```

```py
with open('findme.txt', 'r') as f:
    text = f.read().split(' ')[:-1]
    # print(text)

    result = ''

    for num in text:
        result += chr(int(num))

print(result)

# Corrected the mode from 'wr' to 'w'
with open('result.txt', 'w') as f:
    f.write(result)
```
