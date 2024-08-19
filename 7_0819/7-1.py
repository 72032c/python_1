def play_game():
    min=1
    max=100
    count=0
    ans=random.randint(min,max+1)
    print("======猜數字遊戲======")
    while True:
        count+=1
        keyin=pyip.inputInt(f"請猜數字,範圍:{min}~{max}\n",min=min,max=max)
        if keyin==ans:
            print(f"您猜對了! 答案為{ans}")
            print(f"您猜了{count}次")
            break
        elif keyin>ans:
            max=keyin-1
        elif keyin<ans:
            min=keyin+1

import random
import pyinputplus as pyip
while True:
    play_game()
    yesno=pyip.inputYesNo("您還要繼續猜數字嗎?(y or n)")
    if yesno=="no":
        break
print("應用程式結束")