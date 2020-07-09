import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grads='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grads[i]


if __name__ == '__main__':
    scores = [55, 76, 90]
    for score in scores:
        level = grade(score)
        print(score, '->', level)

    # bisect_left 和 bisect_right 在90分时存在差异

    