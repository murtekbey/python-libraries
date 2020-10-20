import pandas as pd
import numpy as np

personeller = {
    'Çalışan' : ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman' : ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları'],
    'Yaş' : [30,25,45,50,23,34,42],
    'Semt' : ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
    'Maaş' : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df

result = df['Maaş'].sum() # Maaş toplamı
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# for name, group in df.groupby("Semt"): # Semtlere göre gruplandırma yaptık.
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"): # Departmanlara göre gruplandırma yaptık.
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy") # Kadıköyde oturan kişiler.
result = df.groupby("Departman").get_group("Muhasebe") # Muhasebede çalışan kişiler.

result = df.groupby("Departman").sum() # Tüm departman gruplarının ayrı ayrı maaş ve yaş toplamları gelir.
result = df.groupby("Departman").mean() # Yaş ortalaması ve Maaş ortalaması.
result = df.groupby("Departman")["Maaş"].mean() # Sadece departmanların maaş ortalaması hesaplanır.
result = df.groupby("Semt")["Yaş"].mean() # Sadece semtde yaşayanların yaş ortalaması hesaplanır.
result = df.groupby("Semt")["Çalışan"].count() # Semtlere göre çalışan sayısı.
result = df.groupby("Departman")["Yaş"].max() # Departman-Max yaş
result = df.groupby("Departman")["Maaş"].min() # Departman-Min maaş
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"] # Muhasebe departmanında alınan maximum maaş.

result = df.groupby("Departman").agg(np.mean) # Numpy
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]) # Maaş -> Toplam,Ortalama,Max,Min
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"] # Sadece muhasebe için 
print(result)