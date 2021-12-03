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

def diagnostics(df,type='oxygen'):
    df = df['col'].str.split('',expand=True)
    las_col = len(df.columns) - 1
    df  = df.drop(columns=[0,las_col])

    for col in df.columns:
        if len(df[col].value_counts().index.values) == 2:
            if df[col].value_counts().values[0] == df[col].value_counts().values[1]:
                if type == 'oxygen':
                    df = df[df[col] == '1']
                    if len(df.index)== 1 or len(df.index)== 2:
                        return int(''.join(df.iloc[0]))
                else:
                    df = df[df[col] == '0']
                    if len(df.index)== 1 or len(df.index)== 2:
                        return int(''.join(df.iloc[0]))
            else:
                if type == 'oxygen':
                    vals = df[col].value_counts().index.values[0]
                    df = df[df[col] == vals]
                else:
                    vals = df[col].value_counts().index.values[1]
                    df = df[df[col] == vals]
        else:
            if len(df.index) == 1 or len(df.index)== 2:
                return int(''.join(df.iloc[0]))
            else:
                pass


with open('aoc_d3.txt') as f:
    lines = f.read().split('\n')

# Remove last empty item in the list
lines.pop()

df = pd.DataFrame({'col':lines})

oxygen = diagnostics(df,type='oxygen')
co2 = diagnostics(df,type='co2')
print(f'Result: {binaryToDecimal(oxygen) * binaryToDecimal(co2)}')
