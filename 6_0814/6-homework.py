#請修改以下程式碼,計算完成後,問使用者還要繼續('q':離開,enter:繼續)嗎?

while True:
    name=str(input("請輸入姓名:(輸入q再按enter離開)"))
    if name=='q':
        print("應用程式結束")
        break
    try:
        height=float(input('請輸入身高:'))
        weight=float(input('請輸入體重:'))
        BMI=round(weight/(height*0.01)**2,ndigits=2)
        if BMI<18.5:
            grade="過輕"
        elif BMI<24:
            grade="正常"
        elif BMI<27:
            grade="過重"
        elif BMI<30:
            grade="輕度肥胖"
        elif BMI<35:
            grade="中度肥胖"
        elif BMI>=35:
            grade="重度肥胖"
        print(f"{name}的BMI為{BMI}\n體重:{grade}")
    except ValueError:
        print("格式錯誤")