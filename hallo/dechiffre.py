import plotly.express as px
from collections import Counter

from pandas import DataFrame
import pandas as pd

word = "evngeptzigwgeetrrfiftrifefcurafglvczexozpgsvtvofdvetefahahsoorrgejnoeftwhgdvekenrgvgngektcaanmuneesphaeqeaeftuezefvrrsaksgwrrveauadvirngoxtqamuwiaecrsemifemnqkbmhaxtrdsrftrlduagrifefsnczvrruadtfevnwrzevnmntevnwrtefcziphgegdrrrifeeeekdarrhnyzhlvexeenqiwhrrnukfbrqejuagoeadrrrrktrlyufgriaeksblphwngektwsyirgliadrrkteiagwngeabwgeeazmntdrrooetnnrauljakbrdrulegdnskjrdrrkagzfojgsÊytagxoaslrhirrlsriammsfuzdaeaogwwnqitefiafbreagibnwnmuiejmvtgednbhaevaoevwacutvgwdrtnidsnufzmlnsfefevn:wgeetrr?trxgksnafhejvrrfczirdrnwzjepkwgrnhtrtjeedwnjirzmmoevshirlsuwrxuezwbyotajtvkrlrufazmwnsafsmnteavgnnrgiceyncrgdhkgbwspheeabhntefwrroelektrsgzvayeeeqirntevteawgroqejayshetuagvnkcurritkhrfefuzkbnrifibnmnqpeawgaaazruheoefteogzkevnrrcurrmecaanrifsblphwrgektwiaexlsrrbbtkcuastneemvtleynhnvmhsfdsbriqefgeuaddeteadwnnnsojdrrhnyeaaaslrhkgujgeazmstvkhnvsgiyiktvktefurgrn"
word = word.replace(" ", "")

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'ẞ']


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


prim_factors = []

for i in range(len(word)):
    a = word[i - 2] + word[i - 1] + word[i]
    b = word.count(a)
    c = list(find_all(word, a))
    if b == 1:
        continue
    elif b == 2:
        for i in range(len(prime_factors(max(c) - min(c)))):
            prim_factors.append(prime_factors(max(c) - min(c))[i])
        print(f"{a}: {b} at indexes {c}")
    else:
        print(f"{a}: {b} at indexes {c}")

data = {'prime_factor': [], 'count': []}
distinct_vals = set(prim_factors)
for val in distinct_vals:
    count = prim_factors.count(val)
    data['prime_factor'].append(val)
    data['count'].append(count)



df = pd.DataFrame(data)
print(df.to_markdown())

fig = px.bar(df, x='prime_factor', y='count')
fig.show()