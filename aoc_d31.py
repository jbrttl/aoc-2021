import pandas as pd

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


with open('aoc_d3.txt') as f:
    lines = f.read().split('\n')

# Remove last empty item in the list
lines.pop()

bits_g = []
bits_e = []

df = pd.DataFrame({'col':lines})

df = df['col'].str.split('',expand=True)
df  = df.drop(columns=[0,13])

for col in df.columns:
    vals = df[col].value_counts()
    bits_g.append(vals.index.values[0])
    if vals.index.values[0] == '0':
        bits_e.append('1')
    else:
        bits_e.append('0')

print(bits_g)
print(bits_e)

gamma = int(''.join(bits_g))
print(gamma)
epsilon = int(''.join(bits_e))
print(epsilon)

print(f'Result: {binaryToDecimal(gamma) * binaryToDecimal(epsilon)}')
