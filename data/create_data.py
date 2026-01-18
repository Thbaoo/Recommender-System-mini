import pandas as pd 

data = [
	{"user_id": "U1", "product_id": "P1", "rating": 2},
	{"user_id": "U2", "product_id": "P2", "rating": 2},
	{"user_id": "U3", "product_id": "P3", "rating": 3},
	{"user_id": "U3", "product_id": "P1", "rating": 5},
	{"user_id": "U2", "product_id": "P1", "rating": 4},

]

df = pd.DataFrame(data)

df.to_csv("transaction.csv",index=False)

print("Đã tạo file transaction.csv")