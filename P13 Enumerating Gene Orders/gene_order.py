import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16])
plt.ylabel('some numbers')
plt.show()


def find_minimum(list_of_numbers):
    smallest_seen = float('inf')
    for i in list_of_numbers:
        if i < smallest_seen:
            smallest_seen = i

    return smallest_seen

def find_minimum(list_of_numbers):
    smallest_seen = None
    for i in list_of_numbers:
        if (smallest_seen == None) or (i < smallest_seen):
            smallest_seen = i

    return smallest_seen