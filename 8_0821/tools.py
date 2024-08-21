def bmi(bmi:float)->str:
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