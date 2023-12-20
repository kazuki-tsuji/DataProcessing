import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

class import_data:
    
    def import_csv():
        return 0
    
class processing:

    def ks_test(data1,data2):
        pv1 = stats.kstest(data1, "norm")[1]
        pv2 = stats.kstest(data2, "norm")[1]
    
        if pv1 > 0.05:
            if pv2 > 0.05:
                return True,pv1,pv2
            else: 
                return False,pv1,pv2
        else:
            return False,pv1,pv2
            
    def test(parametric,data1,data2):
        if parametric:
            p = stats.ttest_rel(data1,data2)
        else:
            p = stats.wilcoxon(data1,data2)[0]

        if p < 0.05:
            return p,True
        else:
            return p,False
            
input_data1 = [4.70, 3.91, 2.00, 1.81, 1.55]
input_data2 = [4.53, 1.93, 1.75, 1.96, 4.23]       

normary,p1,p2 = processing.ks_test(input_data1,input_data2)

if normary:
    print('正規分布っぽい')
else:
    print('正規分布ではない')

p_value,deff = processing.test(normary,input_data1,input_data2)  

if deff:
    print('有意差あり')
else:
    print('有意差なし') 