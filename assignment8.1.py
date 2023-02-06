def multiplication(f1,f2):
    result = {}
    result['s'] = f1['s']*f2['s']
    result['m'] = f1['m']*f2['m']
    return result

def sum(f1,f2):
    result = {}
    result['s'] = (f1['s']*f2['m'])+(f2['s']*f1['m'])
    result['m'] = f1['m']*f2['m']
    return result   

def division(f1,f2):
    result = {}
    result['s'] = f1['s']*f2['m']
    result['m'] = f1['m']*f2['s']
    return result

def subtraction(f1,f2):    
    result = {}
    result['s'] = (f1['s']*f2['m'])-(f2['s']*f1['m'])
    result['m'] = f1['m']*f2['m']
    return result

a = {"s":2, "m":3}
b = {"s":5, "m":4}

mulresult = mul(a, b)
sumresult = sum(a, b)
divresult = div(a, b)
subresult = sub(a, b)

print("multiplication: ", mulresult)
print("sum: ", sumresult)
print("division: ", divresult)
print("subtraction", subresult)