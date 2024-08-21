from widget import MyClass

while True:
    name=str(input("請輸入姓名:(輸入q再按enter離開)"))
    if name=='q':
        break
    try:
        height=float(input('請輸入身高:'))
        weight=float(input('請輸入體重:'))
        bmi=round(weight/(height*0.01)**2,ndigits=2)
        grade=MyClass.get_bmi(bmi)
        print(f"{name}的BMI為{bmi:.2f}\n體重:{grade}")
    except ValueError:
        print("格式錯誤")
    
print("應用程式結束")