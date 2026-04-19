print("BMI 计算工具")
print("-" * 30)

height = input("请输入身高（cm）：")
weight = input("请输入体重（kg）：")

try:
    height = float(height)
    weight = float(weight)

    if height <= 0 or weight <= 0:
        print("身高和体重必须大于0")
    else:
        bmi = weight / ((height / 100) ** 2)
        print(f"\n你的 BMI 值：{bmi:.1f}")

        if bmi < 18.5:
            print("分类：偏瘦")
        elif bmi < 24:
            print("分类：正常")
        elif bmi < 28:
            print("分类：偏胖")
        else:
            print("分类：肥胖")
except ValueError:
    print("请输入有效的数字")
