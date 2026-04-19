import random

number = random.randint(1, 100)
chances = 7

print("猜数字游戏（1-100）")
print(f"你有 {chances} 次机会\n")

for i in range(chances):
    guess = input(f"第 {i+1} 次猜测：")

    try:
        guess = int(guess)

        if guess == number:
            print(f"🎉 恭喜你猜对了！答案是 {number}")
            break
        elif guess > number:
            print("太高了")
        else:
            print("太低了")

        if i == chances - 1:
            print(f"\n游戏结束！正确答案是 {number}")
    except ValueError:
        print("请输入有效的数字")
