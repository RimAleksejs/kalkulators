

# TO_DO paņemt lietotāja ievadi
import math


def varbutība(a , z):
    return a/z * 100



# TO_DO aprēķināsim varbūtību

# TO_DO salidzināsīm varbūtības

def salidzinājums(x,y):
    return x > y

# TO_DO veiksmigākais spēles komunikāciju aprēķināsana
def kombinacijas(x):
    return math.factorial(x)

if __name__ == '__main__':
    # input no pirmas spēles, divi mainīgie: cikOne , nocikOne
    # ievades parbaude

    cikOne = int(input ("x1"))
    nocikOne = int(input("x2"))

    if cikOne > nocikOne:
        print("nav iespejams")
        exit(0)

        # input no pirmas spēles, divi mainīgie: cikOne , nocikOne
        # ievades parbaude

    cikTwo = int(input("y1"))
    nocikTwo = int(input("y2"))
    if int(cikTwo) > int(nocikTwo):
        print("nav iespejams")
        exit(0)


    pirma = varbutība(cikOne , nocikOne)
    print("Pirma varbutība ir", round(pirma), "% ")

    otra = varbutība(cikTwo , nocikTwo)
    print("Otra varbutība ir", round(otra), "%")

    thebest = salidzinājums(pirma,otra)
    if thebest == True:
        komb1 = kombinacijas(cikOne)
        kombinacijas(cikOne)
        print(cikOne, "Tu vari izveidot", komb1, "savadākas kombinācijās")
    if thebest == False:
        komb2 = kombinacijas(cikTwo)
        print("No", cikTwo, "Tu vari izveidot", komb2, "savadākas kombinācijās")
        kombinacijas(cikTwo)
    else:
        print("Error")
        exit(0)


