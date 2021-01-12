import random

print("事件决断器 by Hurrieam on 20191208")
print("欢迎使用事件决断器！当你不知道很多事情首先该该做什么，然后做什么的时候，可以让此程序帮你进行决断。\n")

print("请直接使用汉语表达您所需要做的所有事情，按回车结束。当所有事件输入完毕后，输入f 回车结束。")

things = []
thing = ""

while thing != "f":
    thing = str(input(">>"))
    if thing != "f":
        things.append(thing)

random.shuffle(things)

for i in range(0, len(things), 1):
    print("您第" + str(i + 1) + "件需要做的事是" + things[i])
input()