import numpy as np



y_true = [0, 1, 1, 0]
y_pred = [0, 1, 0, 0]

def weigh_accuracy(y_true, y_pred,):
    score = 0
    total_weight = 0

    for true, pred in zip(y_true, y_pred):
        if true == 0:
            weight = 1
        else:
            weight = 2
        total_weight += weight    

        if true == pred:
            score += weight

    print("Total score",score) 
    print("Total weight",total_weight)   

    return score / total_weight   





print(weigh_accuracy(y_true, y_pred))
   