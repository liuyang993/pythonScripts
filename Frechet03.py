import math
def euclidean_metric(pa,pb):
    return math.sqrt((pa[0]-pb[0])**2 + (pa[1]-pb[1])**2 )

def one_way_hausdorff_distance(sa,sb):
    distance=0.0
    for pa in sa:
        shortest = 9999999
        for pb in sb:
            dis = euclidean_metric(pa,pb)
            if dis < shortest:
                shortest=dis
        if shortest > distance:
            distance=shortest
    return distance

def hausdorff_distance(sa,sb):
    dis_a=one_way_hausdorff_distance(sa,sb)
    dis_b=one_way_hausdorff_distance(sb,sa)
    return dis_a if dis_a>dis_b else dis_b

A=[(0,0),(1,0),(2,0),(3,0),(4,0)]
B=[(0,3),(1,3),(2,3),(3,3),(3,2),(4,2)]

#print(one_way_hausdorff_distance(A,B))
print(hausdorff_distance(A,B))
