import math
import random

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0

def f(x):
    return 54 * pow(x, 6) + 45 * pow(x, 5) - 102 * pow(x, 4) - 69 * pow(x, 3) + 35 * pow(x, 2) + 16 * x - 4


def prwth_paragwgos(x):
    return 324 * pow(x, 5) + 225 * pow(x, 4) - 408 * pow(x, 3) - 207 * pow(x, 2) + 70 * x + 16


def deuterh_paragwgos(x):
    return 1620 * pow(x, 4) + 900 * pow(x, 3) - 1224 * pow(x, 2) - 414 * x + 70


def newton_raphson(x):
    return x - (1 / (prwth_paragwgos(x) / f(x) - 0.5 * deuterh_paragwgos(x) / prwth_paragwgos(x)))


def temnousa(x, y, z):
    return z - ((f(z) / f(y) * (f(z) / f(y) - f(x) / f(y)) * (z - y) + (1 - f(z) / f(y)) * f(z) / f(x) * (z - x)) /
                ((f(x) / f(y) - 1) * (f(z) / f(y) - 1) * (f(z) / f(x) - 1)))


def dixotomhsh(a, b):
    p = 0
    while True:
        m = random.uniform(a, b)
        p = p + 1
        if f(m) * f(a) < 0:
            b = m
        else:
            a = m
        if (b - a) <= 0.00005:
            break
    return p, m


u = -2
while True:
    unew = newton_raphson(u)
    count1 = count1 + 1
    if abs(unew - u) < 0.00005:
        break
    u = unew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-2, -1.1) με τη μέθοδο Newton - Raphson είναι η " +
      str(unew) + " και έγιναν " + str(count1) + " επαναλήψεις.")

v = -1
while True:
    vnew = newton_raphson(v)
    count2 = count2 + 1
    if abs(vnew - v) < 0.00005:
        break
    v = vnew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1.1, 0.36] με τη μέθοδο Newton - Raphson είναι η " +
      str(vnew) + " και έγιναν " + str(count2) + " επαναλήψεις.")

w = 0.2
while True:
    wnew = newton_raphson(w)
    count3 = count3 + 1
    if abs(wnew - w) < 0.00005:
        break
    w = wnew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1.1, 0.36] με τη μέθοδο Newton - Raphson είναι η " +
      str(wnew) + " και έγιναν " + str(count3) + " επαναλήψεις.")

k = 0.7
while True:
    knew = newton_raphson(k)
    count4 = count4 + 1
    if abs(knew - k) < 0.00005:
        break
    k = knew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα (0.36, 0.98) με τη μέθοδο Newton - Raphson είναι η " +
      str(knew) + " και έγιναν " + str(count4) + " επαναλήψεις.")

l = 1.5
while True:
    lnew = newton_raphson(l)
    count5 = count5 + 1
    if abs(lnew - l) < 0.00005:
        break
    l = lnew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [0.98, 2] με τη μέθοδο Newton - Raphson είναι η " +
      str(lnew) + " και έγιναν " + str(count5) + " επαναλήψεις.\n")


a = -2
b = -1.199
for k in range(15):
    m1 = random.uniform(-2, -1.199)

    if f(m1) == 0:
        count = count + 1
        print("Το " + str(m1) + "είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m1) != 0:
        if f(m1) * f(a) < 0:
            b = m1
        else:
            a = m1

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-2, -1.1) με τη μέθοδο της διχοτόμησης είναι η " +
      str(m1) + " και έγιναν 15 επαναλήψεις.")

c = -1.1
d = -0.18
for k in range(15):
    m2 = random.uniform(-1.1, -0.18)

    if f(m2) == 0:
        count = count + 1
        print("Το " + str(m2) + "είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m1) != 0:
        if f(m2) * f(c) < 0:
            d = m2
        else:
            c = m2

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1.1, 0.36] με τη μέθοδο της διχοτόμησης είναι η " +
      str(m2) + " και έγιναν 15 επαναλήψεις.")

e = -0.181
g = 0.36
for k in range(14):
    m3 = random.uniform(-0.18, 0.36)

    if f(m3) == 0:
        count = count + 1
        print("Το " + str(m3) + "είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m3) != 0:
        if f(m3) * f(e) < 0:
            g = m3
        else:
            e = m3

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1.1, 0.36] με τη μέθοδο της διχοτόμησης είναι η " +
      str(m3) + " και έγιναν 14 επαναλήψεις.")

h = 0.361
i = 0.979
for k in range(14):
    m4 = random.uniform(0.361, 0.979)

    if f(m4) == 0:
        count = count + 1
        print("Το " + str(m4) + "είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m4) != 0:
        if f(m4) * f(h) < 0:
            i = m4
        else:
            h = m4

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα (0.36, 0.98) με τη μέθοδο της διχοτόμησης είναι η " +
      str(m4) + " και έγιναν 14 επαναλήψεις.")

j = 0.98
n = 2
for k in range(15):
    m5 = random.uniform(0.98, 2)

    if f(m5) == 0:
        count = count + 1
        print("Το " + str(m5) + "είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m5) != 0:
        if f(m5) * f(j) < 0:
            n = m5
        else:
            j = m5

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [0.98, 2] με τη μέθοδο της διχοτόμησης είναι η " +
      str(m5) + " και έγιναν 15 επαναλήψεις.\n")

u = -2
v = -1.5
q = -1.199
while True:
    t1 = temnousa(u, v, q)
    count6 = count6 + 1
    if abs(t1 - q) < 0.00005:
        break
    v = q
    q = t1
    t1 = u
print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-2, -1.1) με τη μέθοδο της τέμνουσας είναι η " +
      str(t1) + " και έγιναν " + str(count6) + " επαναλήψεις.")

u1 = -1.1
v1 = -1
q1 = -0.18
while True:
    t2 = temnousa(u1, v1, q1)
    count7 = count7 + 1
    if abs(t2 - q1) < 0.00005:
        break
    v1 = q1
    q1 = t2
    t2 = u1
print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1.1, -0.18] με τη μέθοδο της τέμνουσας είναι η " +
      str(t2) + " και έγιναν " + str(count7) + " επαναλήψεις.")

u2 = -0.181
v2 = 0
q2 = 0.36
while True:
    t3 = temnousa(u2, v2, q2)
    count8 = count8 + 1
    if abs(t3 - q2) < 0.00005:
        break
    v2 = q2
    q2 = t3
    t3 = u2
print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα (-0.18, 0.36] με τη μέθοδο της τέμνουσας είναι η " +
      str(t3) + " και έγιναν " + str(count8) + " επαναλήψεις.")

u3 = 0.361
v3 = 0.7
q3 = 0.979
while True:
    t4 = temnousa(u3, v3, q3)
    count9 = count9 + 1
    if abs(t4 - q3) < 0.00005:
        break
    v3 = q3
    q3 = t4
    t4 = u3
print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα (0.36, 0.98) με τη μέθοδο της τέμνουσας είναι η " +
      str(t4) + " και έγιναν " + str(count9) + " επαναλήψεις.")

u4 = 1
v4 = 1.5
q4 = 2
while True:
    t5 = temnousa(u4, v4, q4)
    count10 = count10 + 1
    if abs(t5 - q4) < 0.00005:
        break
    v4 = q4
    q4 = t5
    t5 = u4
print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [0.98, 2] με τη μέθοδο της τέμνουσας είναι η " +
      str(t5) + " και έγιναν " + str(count10) + " επαναλήψεις.\n")

print("Εκτελώντας τον αλγόριθμο της διχοτόμησης 10 φορές προκύπτουν τα εξής: ")
print(str(dixotomhsh(-1.5, -1.2)))
print(str(dixotomhsh(-1.9, -1.5)))
print(str(dixotomhsh(-1, -0.6)))
print(str(dixotomhsh(-0.7, -0.2)))
print(str(dixotomhsh(0, 0.3)))
print(str(dixotomhsh(-0.1, 0.2)))
print(str(dixotomhsh(0.4, 0.9)))
print(str(dixotomhsh(0.6, 0.8)))
print(str(dixotomhsh(1, 1.7)))
print(str(dixotomhsh(1.5, 1.9)))

print("Παρατηρώ ότι δεν συγκλίνει πάντα στον ίδιο αριθμό επαναλήψεων!")
