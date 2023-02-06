def sum(t1,t2):
    result = {}
    result['h'] = t1['h']+t2['h']
    result['m'] = t1['m']+t2['m']
    result['s'] = t1['s']+t2['s']

    if result['s'] >= 60:
       result['s'] -= 60 
       result['m'] += 1
    if result['m'] >= 60:
       result['m'] -= 60 
       result['h'] += 1

    return result

def sub(t1,t2):
    result = {}
    result['h'] = t1['h']-t2['h']
    result['m'] = t1['m']-t2['m']
    result['s'] = t1['s']-t2['s']       

    if result['s'] < 0:
       result['s'] += 60 
       result['m'] -= 1
    if result['m'] < 60:
       result['m'] += 60 
       result['h'] -= 1

    return result

def show(time):
    print(time['h'],':',time['m'],':',time['s'])

T1 = {'h':8,'m':18,'s':40} 
T2 = {'h':2,'m':30,'s':45}    
resultsum = sum(T1,T2)
resultsub = sub(T1,T2)

print(resultsum)
print(resultsub)