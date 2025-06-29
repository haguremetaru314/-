Ob=input("「オーバーヒート」を使用した回数を整数で教えてください\n使用していないなら「0」と入力してください　　")
Ob=int(Ob)
Oc=2**Ob-1
N=input("「ねじれ触手」をダメージを分割できる回数を整数で教えてください\n使用していないなら「1」と入力してください　　")
N=int(N)
X=input("あなたの与えるダメージの増加量、相手の受けるダメージの増加量の合計を整数で教えてください\n使用していないなら「0」と入力してください　　")
X=int(X)
R=input("「羅刹の拳」によるダメージの倍率を整数で教えてください\n使用していないなら「1」と入力してください　　")
R=int(R)
import math
def my_sum(a):
  if (N!=1)and((a+X)*R/N>=1):
    b=math.floor(((a+X)*R/N)+X)*R*N
    nF=1
  else:
    b=(a+X)*R
    nF=0
  return b,nF
rD,rDnF=my_sum(Oc+1)
mD,mDnF=my_sum(rD*(Oc+4))
aD=rD*(Oc+4)+mD
if (rDnF==1):
   print("\n通常版「撫で斬り」の連撃は",rD/N,"ダメージを",(Oc+4)*N,"回")
else:
   print("\n通常版「撫で斬り」の連撃は",rD,"ダメージを",(Oc+4),"回")
if (mDnF==1):
  print("最後のダメージは",mD/N,"ダメージを",N,"回")
else:
  print("最後のダメージは",mD,"ダメージ")
print("合計",aD,"ダメージ")
input("Enterキーを押すと終了します")

