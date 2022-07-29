''' we creating a dataframe with the help of dictionaries '''
# a={"1":[1,2,3,4],
#        "2":['niharika','pravalika','niha','prava'],
#        "3":['aug','may','june','july'],
#        "4":['python','html','java','css']
#        }


# print(a,type(a))
# import pandas as pd
# df2=pd.DataFrame(a)
# print(df2)

''' we now create a dataframe with the help of tuples '''
# import pandas as pd
# a=[(1,"Niharika","Python"),(2,"Pravalika","Python"),(3,"Ramya","Advanced Python"),(4,"Akhila","Java"),(5,"Shravani",'C')]
# df3=pd.DataFrame(a,columns=["S.no","Name","Course"])
# print(df3)


# import pandas as pd
# f=pd.read_csv('10b.csv')
# print(f)

# import pandas as pd
# f=pd.read_excel('b100.xlsx')
# print(f)
    
    
    
# import pandas
# d=pandas.read_csv("B5.csv")
# print(d)
# print(d.shape) # shape method will show how many rows and columns
# print(d.head()) # head method will show first 5 rows data
# print(d.tail())  # tail method will print last 5 rows data
# print(d.head(1))
# print(d.tail(3))
# print(d[:]) # it will print all the rows in the table
# print(d[2:6])
# print(d[1:4])
# print(d.columns)
# print(d.Place)
# print(d[['Place','Name']])
# print(d)
# print(d['sal'].max())
# print(d['sal'].min())
# print(d.describe())
# print(d[d.sal>400])
# print(d['Place'][d.sal>400])
# print(d[d.sal<450])
# print(d[d.sal==d.sal.max()])
# print(d)
# print(d.loc[5])
# d1=d.set_index('ID')
# print(d1)