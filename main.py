from myMATH import myArithmetic
from myMATH import myCalcArea
from myMATH import myStatistics
def LIST() :
    l = []
    n = int(input("請輸入欲計算的數據總數目")) 
    N = 0
    while True :
        N +=1
        y = int(input("請輸入第" + str(N) + "筆數值"))
        l.append(y)
        if N == n :
            break
    print("所算得之平均值為"+str(myStatistics.myMean(l)))
LIST()


