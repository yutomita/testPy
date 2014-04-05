# -*- coding: utf-8 -*-

oneStep = 3
goal = 30

count = 0

def test2(cn, val, sp):
    for i in range(1, sp + 1):
        one = val - i
        if one > 0:
            cn = test2(cn, one, sp)
        elif one == 0:
            cn += 1
    return cn

print str(goal) + "段最大" + str(oneStep) + "段上れる場合の"
print "組み合わせは"
print test2(count, goal, oneStep)
print "です"

