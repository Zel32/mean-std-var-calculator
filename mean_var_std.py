import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    list_flat = list;
    list_2d = np.reshape(list,(3,3));

    # mean
    mean_a1 = np.mean(list_2d,0)
    mean_a2 = np.mean(list_2d,1)
    mean_flat = np.mean(list_flat)

    mean_list = [mean_a1.tolist(), mean_a2.tolist(), mean_flat.tolist()]

    # variance
    var_a1 = np.var(list_2d,0)
    var_a2 = np.var(list_2d,1)
    var_flat = np.var(list_flat)

    var_list = [var_a1.tolist(), var_a2.tolist(), var_flat.tolist()]

    # standard deviation
    std_a1 = np.std(list_2d,0)
    std_a2 = np.std(list_2d,1)
    std_flat = np.std(list_flat)

    std_list = [std_a1.tolist(), std_a2.tolist(), std_flat.tolist()]

    # max
    max_a1 = np.max(list_2d,0)
    max_a2 = np.max(list_2d,1)
    max_flat = np.max(list_flat)

    max_list = [max_a1.tolist(), max_a2.tolist(), max_flat.tolist()]

    # min
    min_a1 = np.min(list_2d,0)
    min_a2 = np.min(list_2d,1)
    min_flat = np.min(list_flat)

    min_list = [min_a1.tolist(), min_a2.tolist(), min_flat.tolist()]

    # sum
    sum_a1 = np.sum(list_2d,0)
    sum_a2 = np.sum(list_2d,1)
    sum_flat = np.sum(list_flat)

    sum_list = [sum_a1.tolist(), sum_a2.tolist(), sum_flat.tolist()]

    # create dictionary output
    calculations = {
        'mean': mean_list,
        'variance': var_list,
        'standard deviation': std_list,
        'max': max_list,
        'min': min_list,
        'sum': sum_list}
#     for key, value in results.items():
#         print(f"{key}: {value}")



    return calculations