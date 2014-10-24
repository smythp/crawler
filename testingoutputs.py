x = ['ham','egg','cheese']
y = ['egg','monkey','ham','bacon']
for item in x:
    print('checking',item)
    if item in y:
        print(item,' present in y')
