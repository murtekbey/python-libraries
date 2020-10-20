import pandas as pd

list = [["Murat",50],["Gurur",60],["Anıl",70],["Efe",80]]
dict = {'Name': ['Murat','Gurur','Anıl','Efe'],'Grade': [50,60,70,80]}
dict_list = [
                {"Name":"Murat","Grade":50},
                {"Name":"Gurur","Grade":60},
                {"Name":"Anıl","Grade":70},
                {"Name":"Efe","Grade":80}
            ]


# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(data, columns = ['Name','Grade'], index = [1,2,3,4], dtype = float)
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ['212','232','236','456']) # index numaralarını bu şekilde değiştirebiliriz.
df = pd.DataFrame(dict_list,index = [1,2,3,4])

print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)