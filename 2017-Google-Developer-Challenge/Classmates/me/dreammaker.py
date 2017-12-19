# -*- coding: utf-8 -*-
"""
20171218
This program will help you to achieve your dreams

This program is open source, feel free to copy modify and share. Just let the author know the changes :)

Author: Jaime Andres Cataño Bernal
email: jaimeandrescatano@gmail.com
"""

def verificar(var1, var2):
    while True:
        if var1 != "yes":
            if var1 != "no":
                print "\nPlease answer yes, or no!"
                var1 = raw_input(var2)
            else:
                salida = "no"
                break
        else:
            salida = "yes"
            break
    return salida

print """
import memories
from live import experience
"""

sep = "**********************************************************"

print "go out of the comfort zone"
print "learn"
print "try a bit of the panic zone"
print "collect information from the panic zone"
print "go to the comfort zone"
print "pick up resources"
print "go to the learning zone"
print "pick up resources"

print "\nDefine the main plan, a backup plan and the emergency plan"

plans = ["Main plan", "Backup plan", "Emergency plan",]

plansDone = [1,2,3]
i=0
for x in plans:
    pregunta = "\nIs %s done? yes/no \n\n" % x
    mico = raw_input(pregunta)
    plansDone[i] = verificar(mico, pregunta)
    i=i+1

i=0
w=0
for x in plansDone:
    if x != "yes":
        print "\nYou need to develop a %s!" % (plans[i])
        # print plans[i]
        w=w+1
    i=i+1

if w != 0:
    if w == 1:
        print "\n%s\nJust one more plan and you can go on!\n%s\n" % (sep, sep)
    elif w == 2:
        print "\n%s\nYou are in the correct path, keep going!\n%s\n" % (sep, sep)
    elif w == 3:
        print "\n%s\nR U serius?\n\nI'm sorry to say it but your dreams will never come true!\n\nPlease don't be an obstacle to those who are working for their dreams.\n\nAnd don't forget: somebody else is making his dreams true with your life.\n%s\n" % (sep, sep)
    break

""" Define a suitable validation agents for each plan """
planAvalidators = ["experts", "people already in the panic zone", "other",]
planBvalidators = ["closest people", "other",]
planCvalidators = ["family", "friends", "other",]

plansValidators = [planAvalidators, planBvalidators, planCvalidators,]

# plansValidated = [["yes" for x in range(5)] for y in range(2)]
plansValidated = [["yes" for x in range(len(planAvalidators))], ["yes" for x in range(len(planBvalidators))],["yes" for x in range(len(planCvalidators))],]

i=0
for x in plans:
    print "\n"
    m=0
    for y in plansValidators[i]:
        pregunta = "\nIs %s validated by %s? yes/no \n\n" % (x,y)
        mico = raw_input(pregunta)
        plansValidated[i][m] = verificar(mico, pregunta)

        m=m+1

    i=i+1

i=0
for x in plans:
    print "\n"
    m=0
    for y in plansValidators[i]:

        if plansValidated[i][m] == "no":
            print "\nWe want to minimize the risks as much as posible, please go and get the validation of your %s from the %s\n" % (x,y)

        m=m+1

    i=i+1


print "Execute %s, if it fail then execute %s, if it fail then execute %s" % (plans[0], plans[1], plans[2],)
