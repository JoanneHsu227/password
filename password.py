x = 3 #有三次機會
while x > 0:
	password = input('請輸入密碼')
	if password == "a123456":
	    print('登入成功')
	    break
	else:
		x = x - 1
		print('密碼錯誤，您還剩下' , x , '次機會')
		if x == 0:
			print('忘記密碼請洽管理員')
			


