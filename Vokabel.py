from random import *
from sys import *
English = True
Exit = False
scoor=0
while Exit == False:
    Zufal = randint(1, 48)
    A=1
    if Zufal == A :
        V1="stand up for"
        V2="eintreten / sich einsetzen für"
    A+=1
    if Zufal == A :
        V1="pass"
        V2="genehmigen / verabschieden"
    A+=1
    if Zufal == A :
        V1="declaration"
        V2="Erklärung"
    A+=1
    if Zufal == A :
        V1="symbol"
        V2="Symbol"
    A+=1
    if Zufal == A :
        V1="amendment"
        V2="Änderung"
    A+=1
    if Zufal == A :
        V1="explode"
        V2="explodieren"
    A+=1
    if Zufal == A :
        V1="tax"
        V2="Steuer"
        A+=1
    if Zufal == A :
        V1="bubble"
        V2="Blase"
    A+=1
    if Zufal == A :
        V1="ignore"
        V2="ignorieren"
    A+=1
    if Zufal == A :
        V1="complain"
        V2="beklagen / beschweren"
    A+=1
    if Zufal == A :
        V1="awake"
        V2="wach"
    A+=1
    if Zufal == A :
        V1="sympathetic"
        V2="mitfühlend"
    A+=1
    if Zufal == A :
        V1="concentrate"
        V2="konzentrieren"
    A+=1
    if Zufal == A :
        V1="backwards"
        V2="rückwärts"
        A+=1
    if Zufal == A :
        V1="forwards"
        V2="vorwärts"
    A+=1
    if Zufal == A :
        V1="figure out"
        V2="etwas herausfinden"
    A+=1
    if Zufal == A :
        V1="district"
        V2="Gegend / Bezirk"
    A+=1
    if Zufal == A :
        V1="argument"
        V2="Argument"
    A+=1
    if Zufal == A :
        V1="disagreement"
        V2="Uneinigkeit / Streit"
        A+=1
    if Zufal == A :
        V1="agreement"
        V2="Einigung"
    A+=1
    if Zufal == A :
        V1="challenge"
        V2="herausfordern"
    A+=1
    if Zufal == A :
        V1="lazy"
        V2="faul"
    A+=1
    if Zufal == A :
        V1="no matter"
        V2="ganz gleich / was"
    A+=1
    if Zufal == A :
        V1="make sb. do sth."
        V2="jn. zwingen, etwas zu tun"
    A+=1
    if Zufal == A :
        V1="pressure"
        V2="Druck"
        A+=1
    if Zufal == A :
        V1="debate"
        V2="debatieren"
    A+=1
    if Zufal == A :
        V1="constitution"
        V2="Verfassung"
    A+=1
    if Zufal == A :
        V1="citizenship"
        V2="Staatsangehörigkeit"
    A+=1
    if Zufal == A :
        V1="citizen"
        V2="Bürger"
    A+=1
    if Zufal == A :
        V1="xenophobic"
        V2="fremdenfeindlich"
    A+=1
    if Zufal == A :
        V1="turn into"
        V2="etwas in etwas verwandeln"
        A+=1
    if Zufal == A :
        V1="stare"
        V2="starren"
    A+=1
    if Zufal == A :
        V1="silence"
        V2="Stille"
    A+=1
    if Zufal == A :
        V1="power"
        V2="Macht"
    A+=1
    if Zufal == A :
        V1="on the one hand"
        V2="auf der einen Seite"
    A+=1
    if Zufal == A :
        V1="on the other hand"
        V2="auf der anderen Seite"
        A+=1
    if Zufal == A :
        V1="Congress"
        V2="Kongress"
    A+=1
    if Zufal == A :
        V1="democracy"
        V2="Democratie"
    A+=1
    if Zufal == A :
        V1="democrat"
        V2="Demokrat"
    A+=1
    if Zufal == A :
        V1="democratic"
        V2="demokratisch"
    A+=1
    if Zufal == A :
        V1="absote monarchy"
        V2="absolute Monarchie"
    A+=1
    if Zufal == A :
        V1="anarchy"
        V2="Anarchie"
        A+=1
    if Zufal == A :
        V1="constitutional monarchy"
        V2="konstitutionelle Monarchie"
    A+=1
    if Zufal == A :
        V1="dictatorship"
        V2="Diktatur"
    A+=1
    if Zufal == A :
        V1="junta"
        V2="Militärdiktatur"
    A+=1
    if Zufal == A :
        V1="oligarchy"
        V2="Oligarchie"
    A+=1
    if Zufal == A :
        V1="plutocray"
        V2="Plutokratie"
    A+=1
    if Zufal == A :
        V1="theocracy"
        V2="Theokratie"

   










    if English == True:
        x = input("Was bedeutet: " + V2 +" = ")
        if x =="exit":
            Exit = True
            print(scoor)
        if x == V1 :
            print("Richtig")
            scoor += 1
            English = False
        else: 
            if Exit == False:
                print ("Falsch! Richtig wäre " + V1)
    else :
        if English == False:
            x = input("Was bedeutet " + V1 +" = ")
            if x =="exit":
                Exit = True
            if x == V2 :
                if Exit == False:
                    print("Richtig")
                    scoor += 1
                    English = True
            else: 
                print ("Falsch! Richtig wäre " + V2)
