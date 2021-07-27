distm = float(input('Uma distancia em metros: '))
km = distm * 0.001
hm = distm * 0.01
dam = distm * 0.1
dm = distm * 10
cm = distm * 100
mm = distm * 1000

print('{}mt é igual a: '.format(distm))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))