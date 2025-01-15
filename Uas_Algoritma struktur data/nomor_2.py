import pandas as pd
df= pd.DataFrame(
    [90,50,65],
    [80,60,70]
)
index=['Mahasiswa1','Mahasiswa2','Mahasiswa3'],
columns=['Nama','Algoritma dan struktur data 2','Matematika Numerik']

df['Algoritma'] = [90,50,65]
df['Matematika Numerik'] = [80,60,70]


df.loc['total'] = df.sum(axis=0)
df['rata']=df.mean(axis=1)

print(df)

index_nilai_tertinggi_perbaris = df.idxmax(axis=0)
print(index_nilai_tertinggi_perbaris)
