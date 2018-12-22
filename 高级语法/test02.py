# 功能要求：
# 要求用户输入总资产，例如： 2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# goods=[
# {"name":"电脑","price":1999},
# {"name":"鼠标","price":10},
# {"name":"游艇","price":20},
# {"name":"美女","price":998},
# ]
count = int(input("请输入总资产："))

goods = [{'电脑': 1999}, {'鼠标': 10}, {'游艇': 20}, {'美女': 998}]
print(goods)

computer = goods[0]['电脑']
mouse = goods[1]['鼠标']
youting = goods[2]['游艇']
girl = goods[3]['美女']

buy_car =[]
thing = input('请输入你想购买的物品：')
if thing == '电脑':
    buy_car.append(computer)
if thing == '鼠标':
    buy_car.append(mouse)
if thing == '游艇':
    buy_car.append(youting)
if thing == '美女':
    buy_car.append(girl)
total = sum(buy_car)

if total > count:
    print('余额不足')
