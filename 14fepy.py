セイウチ演算子(代入、比較２つの動作同時に行える）

if (n:=10)>5:

    10/0 ZeroDivisionError

try

except

else(エラーがない時）

finally(エラー発生しても必ず実行する

def generator(max):

  print("作成")

  for n in max:

     yield n

     print("実行")

gen=generator(10)

n=next(gen)

print(n={}.format(n))#作成

　　　　　　　　　　n=0

n=next(gen)

print(n={}.format(n))#実行(１回目のyieldのところまで変える）

　　　　　　　　　n=1

def generator(max):

print("作成")

　for n in max:

　    x=yield n

　    print("実行")

       print(x={}.format(x))

gen=generator(10)

n=next(gen)#ここでnに0入る

gen.send(100)#実行

　　　　　　　100(x=yield nのxに１００おくル）

