a,b= input("通常版「制定の盾」、強化版「制定の盾」の枚数をそれぞれコンマ(,)で区切って教えてください。例: 1,2 --> ").split(",")
a = int(a)
b = int(b)
x=a+b
import math
n=1-((math.factorial(11-b))*(math.factorial(13-b-a))/((math.factorial(10-b))*(math.factorial(11-b-a))*1716))
m = round(n*100,1)
print("特定の1つのルールが選択肢に現れる可能性は",m,"%")
input("Enterキーを押すと終了します")