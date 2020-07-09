import numpy

if __name__ == '__main__':

    my_ary = numpy.arange(12)
    print(my_ary)
    print(type(my_ary))
    print(my_ary.shape)
    my_ary.shape = 3, 4
    print(my_ary)
    print(my_ary[2])
    print(my_ary[2, 1])
    print(my_ary[:, 1])
    my_ary.transpose()
    print(my_ary)