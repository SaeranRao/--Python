x = 100
y = 200
s = 'print(x,y,x+y)'

exec(s) # 100 200 300
exec(s,{'x':10,'y':20}) # 10 20 30
exec(s,{'x':10},{'x':1,'y':2}) # 1 2 3
exec(s,{'x':10},{'y':2}) # 10 2 12