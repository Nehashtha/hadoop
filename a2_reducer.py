#!/usr/bin/env python

import sys
def reducer():
    val=[]
    counter =0
    data = 0
    total_sum=0
    for line in sys.stdin:
        line=line.strip()
        data_str,first_column = line.split('\t',1)
        try:
            data=float(data_str)
            val.append(data)
            counter = counter + 1
            total_sum=total_sum+data
            if counter == 1:
                print("%s \t %s" % ('minimum', data))
        except ValueError:
            continue
    print("%s \t %s" % ('maximum', data))
    avg=total_sum/counter
    diff =0.0
    b=1
    a=0
    normalized_data=[]
    x= len(val)//2
    if len(val)%2==0:
        value=(val[x]+val[x-1])
        med=float(value)/2
        print("%s \t %s" % ('median', med))
    else:
        print("%s \t %s" % ('median', float(val[x])))
    for i in range(len(val)):
        diff = diff + (((float(val[i])) - avg) ** 2)
        norm1 = (float(val[i]) - float(val[0])) / (float(val[-1]) - float(val[0]))
        norm2=norm1* (b-a)
        norm_final=a + norm2
        normalized_data.append(norm_final)
    div = diff / counter
    std = (div) ** (0.5)
    print("%s \t %s" % ('standard deviation', std))
    print("%s \t %s" % ('normalized data', normalized_data ))


reducer()