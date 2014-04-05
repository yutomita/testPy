# -*- coding: utf-8 -*-

human = {
    "A": {"height": 184, "weight": 92},
    "B": {"height": 174, "weight": 68},
    "C": {"height": 163, "weight": 59},
    "D": {"height": 182, "weight": 60},
    "E": {"height": 159, "weight": 71},
    "F": {"height": 170, "weight": 66}
}

print "身長の高い順"
for x, y in sorted(human.items(), key=lambda hei:-hei[1]["height"]):
    print x, y

print "体重の少ない順"
for x, y in sorted(human.items(), key=lambda wei:wei[1]["weight"]):
    print x, y

