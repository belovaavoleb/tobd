import numpy as np

dataset = np.loadtxt('minutes_n_ingredients.csv', delimiter=',', skiprows=1, dtype=np.int32)

# 1
# print(dataset[:5])


# 2
# print(dataset[:, 1:].mean(axis=0),
#      dataset[:, 1:].min(axis=0),
#      dataset[:, 1:].max(axis=0),
#      np.median(dataset[:, 1:], axis=0), sep='\n')


# 3
# new_dataset = np.clip(dataset[:, 1:2], 0, int(np.quantile(dataset[:, 1:2],.75)))
# end = np.concatenate((dataset[:, 0:1], new_dataset, dataset[:, 2:]), axis = 1)
# print(end)


# 4
# print(*(sum(dataset[:, 1:2]==0)))


# 5
# new_dataset = np.unique(dataset[0:, :1])
# print(len(new_dataset))


# 6
# new_dataset = np.unique(dataset[:, 2:])
# print(len(new_dataset))


# 7
# new_dataset = np.where(dataset[:, 2:] <= 5, dataset[:, :], False)
# end_dataset = np.where(new_dataset[:, 0] != 0)
# print(new_dataset[end_dataset])


# 8
# end_dataset = np.where(dataset[:, 1] != 0)
# f_dataset = dataset[end_dataset]
# new_dataset = np.array(f_dataset[:, 2]/f_dataset[:, 1])
# print(max(new_dataset))


# 9
# new_dataset = dataset[dataset[:, 1].argsort()][len(dataset):len(dataset)-100:-1]
# print(sum(new_dataset[2])/100)


# 10
# inx = np.random.randint(0, len(dataset), size=10)
# print(dataset[inx])


# 11
# mid = sum(dataset[:, 2:]) / len(dataset)
# new_dataset = np.where(dataset[:, 2:] <= mid, dataset[:, :], False)
# end = np.where(new_dataset[:, 0] != 0)
# print(len(new_dataset[end]) / len(dataset) * 100)


#12
# new_dataset = np.where((dataset[:, 2:] <= 5)&(dataset[:, 1:2] <= 20), +10**10, -10**10)
# change = np.clip(new_dataset[:, :], 0, 1)
# end_dataset = np.concatenate((dataset[:, :],change), axis = 1)
# print(end_dataset)


#13
# new_dataset = np.where((dataset[:, 2:] <= 5)&(dataset[:, 1:2] <= 20), dataset[:, :], False)
# end = np.where(new_dataset[:, 0] != 0)
# print(len(new_dataset[end]) / len(dataset) * 100)


#14
# group_1 = dataset[dataset[:, 2] <= 10]
# group_2 = dataset[(dataset[:, 2] > 10) & (dataset[:, 2] <= 20)]
# group_3 = dataset[dataset[:, 2] > 20]
# x = min(len(group_1), len(group_2), len(group_3))
# end_dataset =np.stack([group_1[:x],  group_2[:x], group_3[:x]])
# print(end_dataset)
