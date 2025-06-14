def minMaxDifference(num):
    num = list(str(num))
    #Max
    maxEle = num
    i = 0
    while i < len(maxEle)-1:
        if maxEle[i]=='9':
            i+=1
        else:
            break
    maxEle = "".join(maxEle)
    replaceMax = maxEle[i]
    maxEle = int(maxEle.replace(replaceMax,'9'))
    #Min
    minEle = num
    replaceMin = num[0]
    minEle = "".join(minEle)
    minEle = int(minEle.replace(replaceMin,'0'))
    
    return maxEle-minEle

print(minMaxDifference(int(input())))