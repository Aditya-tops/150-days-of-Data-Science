import pandas as pd

details = [
            ["sagar",20,10000],
            ["Daniel",16,20000],
            ["Veeru",24,30000],
            ["Raju",25,40000],
            ["kiran",26,50000],
            ["kedar",27,60000],
            ["reena",28,70000],
            ["kartik",29,80000],
            ["satis",30,90000],
          ]
inx  = [11,22,33,44,55,66,77,88,99]
cols = ["Name","Age","Salary"]

df = pd.DataFrame(details,index=inx,columns=cols)
print(df)