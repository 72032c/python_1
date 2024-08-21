from . import tools

class MyClass:
    @classmethod
    def get_bmi(cls,bmi: float) -> str:
        if bmi<18.5:
            return "過輕"
        elif bmi<24:
            return "正常"
        elif bmi<27:
            return "過重"
        elif bmi<30:
            return "輕度肥胖"
        elif bmi<35:
            return "中度肥胖"
        elif bmi>=35:
            return "重度肥胖"