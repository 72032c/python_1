def get_status_message(bmi: float) -> str:
    if bmi<18.5:
        grade="過輕"
    elif bmi<24:
        grade="正常"
    elif bmi<27:
        grade="過重"
    elif bmi<30:
        grade="輕度肥胖"
    elif bmi<35:
        grade="中度肥胖"
    elif bmi>=35:
        grade="重度肥胖"