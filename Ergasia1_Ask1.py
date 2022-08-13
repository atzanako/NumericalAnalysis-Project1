from math import exp, pow, sin, cos
import matplotlib.pyplot as pl
import numpy as nm
import matplotlib.font_manager as fm

fp1 = fm.FontProperties(fname=r'C:\WINDOWS\Fonts\arial.ttf')


def f(x):
    return nm.e**(nm.sin(3)*x)+(x**6)-2*(x**4)-(x**3)-1


x = nm.linspace(-2, 2, 1000)

pl.title(u'Άσκηση 1 - Εργασία 1', fontproperties=fp1, fontsize=12, color='blue')

pl.axis([-10, 10, -10, 10])

pl.plot(x, f(x), 'r-', linewidth=2.0)

pl.grid(True)
pl.show()



def f(x):
    return exp(pow(sin(x), 3)) + pow(x, 6) - 2 * pow(x, 4) - pow(x, 3) - 1


a = -2
b = -1
c = 2
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

# επειδή το f(-2) και f(2) ειναι θετικά δεν ισχύει το θεώρημα Bolzano στο δίαστημα [-2,2], οποτε το χωρίζουμε σε δύο
# μικρότερα τα [-2, -1] και [-1,2]

print("Το Χ0 = 0 είναι προφανής ρίζα της εξίσωσης f(x)=0.\n")

for k in range(15):
    m1 = (a + b) / 2

    if f(m1) == 0:
        count1 = count1 + 1
        print("Το " + str(m1) + " είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m1) != 0:
        if f(m1) * f(a) < 0:
            b = m1
        else:
            a = m1

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-2, -1] με τη μέθοδο της διχοτόμησης είναι η " + str(m1)
      + " και έγιναν 15 επαναλήψεις.")

for k in range(16):
    m2 = (b + c) / 2
    if f(m2) == 0:
        count2 = count2 + 1
        print("Το " + str(m2) + " είναι ρίζα της εξίσωσης f(x)=0.")
        break

    if f(m2) != 0:
        if f(m2) * f(b) < 0:
            c = m2
        else:
            b = m2

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1, 2] με τη μέθοδο της διχοτόμησης είναι η " + str(m2)
      + " και έγιναν 16 επαναλήψεις.\n")

print("Η f(x) είναι δύο φορές παραγωγίσιμη στο διάστημα [-2, 2], όμως f(-2) * f(2) > 0 οπότε θα χωρίσουμε το διάστημα"
      "σε δύο μικρότερα. Το Ι1 = [-2, -1] και το Ι2 = [-1, 2].\n")


def prwth_paragwgos(x):
    return 3 * pow(sin(x), 2) * cos(x) * exp(pow(sin(x), 3)) + 6 * pow(x, 5) - 8 * pow(x, 3) - 3 * pow(x, 2)


def deuterh_paragwgos(x):
    return 9 * pow(cos(x), 2) * pow(sin(x), 4) * exp(pow(sin(x), 3)) - 3*pow(sin(x), 3) * exp(pow(sin(x), 3)) + 6 \
           * sin(x) * pow(cos(x), 2) * exp(pow(sin(x), 3)) + 30 * pow(x, 4) - 24*pow(x, 2) - 6*x


def nr(x):
    return x - (f(x) / prwth_paragwgos(x))


z = -1.15
while True:
    znew = nr(z)
    count3 = count3 + 1
    if abs(znew - z) < 0.00005:
        break
    z = znew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-2, -1] με τη μέθοδο Newton - Raphson είναι η " +
      str(znew) + " και έγιναν " + str(count3) + " επαναλήψεις.")

k = 1.5
while True:
    knew = nr(k)
    count4 = count4 + 1
    if abs(knew - k) < 0.00005:
        break
    k = knew

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1, 2] με τη μέθοδο Newton - Raphson είναι η " +
      str(knew) + " και έγιναν " + str(count4) + " επαναλήψεις.\n")


def temnousa(x, y):
    return x - f(x) * (x - y) / (f(x) - f(y))


u = -2
v = -1
while True:
    t1 = temnousa(u, v)
    count5 = count5 + 1
    if abs(t1 - v) < 0.00005:
        break
    u = v
    v = t1

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-2, -1] με τη μέθοδο της τέμνουσας είναι η " +
      str(t1) + " και έγιναν " + str(count5) + " επαναλήψεις.")

m = 1.5
n = 2
while True:
    t2 = temnousa(m, n)
    count6 = count6 + 1
    if abs(t2 - n) < 0.00005:
        break
    m = n
    n = t2

print("H προσέγγιση της ρίζας της εξίσωσης f(x)=0 στο διάστημα [-1, 2] με τη μέθοδο της τέμνουσας είναι η " +
      str(t2) + " και έγιναν " + str(count6) + " επαναλήψεις.")
