# 企业发放的奖金根据利润提成。
# 利润低于或等于10万元时，奖金可提10%；
# 利润高 10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%;
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

liRui = int(input('今年的利润是：'))
prise1 = 10 * 0.1
prise2 = prise1 + 10 * 0.075
prise3 = prise2 + 20 * 0.05
prise4 = prise3 + 40 * 0.03
prise5 = prise4 + 60 * 0.0015
prise = 0
if liRui <=10:
    prise = liRui * 0.1
if liRui > 10 and liRui < 20:
    prise = prise1 + (liRui - 10) * 0.075
if liRui > 20 and liRui < 40:
    prise = prise2 + (liRui - 20) * 0.05
if liRui > 40 and liRui < 60:
    prise = prise3 + (liRui - 40) * 0.03
if liRui > 60 and liRui < 100:
    prise = prise4 + (liRui - 60) * 0.0015
if liRui >=100:
    prise = prise5 + (liRui - 100) * 0.01
print(prise)
