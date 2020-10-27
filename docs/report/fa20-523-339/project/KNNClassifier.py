import math;
import heapq
#https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761
def unique(iterable):
    items = list(iterable)
    unique_items = list(set(items))
    counts = [items.count(item) for item in unique_items]
    return unique_items, counts
# here is KNN classifier we perform algorithm
class KNN_Classifier:
    def __init__(self, k):
        self.k = k
    # redefined since we have d-dimension attributes per dataset
    def euclidean_distance(self, point1, point2):
        num=0
        if (len(point1)!=len(point2)):
            print("it should never happened")
            pass
        else:
            for i in range(len(point1)):
                num+= (point1[i] - point2[i]) * (point1[i] - point2[i])
        return math.sqrt(num)
    #pick the most frequent label
    def pick_label(self, top_k_labels):
        list=unique(top_k_labels)
        current=0
        mostfrequentlabel=None
        for i in range(len(list[0])):
            if list[1][i]>current:
                current=list[1][i]
                mostfrequentlabel=list[0][i]
        return mostfrequentlabel
    def classify(self, point, sample_points, sample_labels):
        k=self.k
        fun=lambda s:self.euclidean_distance(s,point)
        lenth=len(sample_points)
        label=[]
        for i in range(lenth):
            label.append((fun(sample_points[i]),sample_labels[i]))
        ourlabel=[]
        for i in range(k):
            label.sort(key=lambda x:x[0])
            value=heapq.heappop(label)
            ourlabel.append(value[1])
        return self.pick_label(ourlabel)
