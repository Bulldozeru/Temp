import math as m

pi = m.pi

calcValues = {

    "z1": 18, # Diztii1
    "z2": 104, # Diztii2
    "mn": 4, # Modulul Nominal
    "beta": 10, # Beta Angle
    "aSTAS": 250, # Roata 2
    "b2/d1": 0.5, # RAPORT
    "Tip Joc": 2,
    "TT": 2,
    "alphaN": 20,

# ================================================== #

    "a0": 247.764093,
    "alphaT":  20.283559,
    "alphaWT": 21.627541,
    "xsn": 0.577,
    "zv1": 18.846,
    "zv2": 108.888 ,
    "xn1": 0.425,
    "xn2": 0.152,
    "mt": 4.061706,
    "d1": 73.110716,
    "d2": 422.417471,
    "dA1": 70.12913,
    "db1": 68.577007,
    "db2": 396.222708,
    "dw1": 73.770492,
    "dw2": 426.229509,
    "df1": 66.510716,
    "df2": 413.633471,
    "da1prel": 84.3,
    "da2prel": 431.4,
    "cn1": 1.044642,
    "cn2": 1.033265,
    "cna": 0.4,
    "da1def": 84,
    "da2def": 431,
    "h1": 8.744642,
    "h2": 8.683265,
    "alphaAt1": 35.274673,
    "alphaAat2": 23.174551,



    "sat1": 2.37781,
    "sat2": 3.50628,
    "sata": 1.6,
    "b2": 37,
    "b1": 40,
    "dl1": 69.632111,
    "dl2": 416.038597,
    "dE2": 418.840725,
    "epsyAlpha": 1.413533,
    "epsyBeta": 0.511284,
    "epsyGamma": 1.924817,
    "zmin1": 9.830927,
    "zmin2": 14.49848,
    "N1":3,
    "N2": 13,
    "WNn1": 31.737627,
    "WNn2": 154.109034,
    "b1min": 10.511181,
    "b2min": 31.760753,


}

calcAngles = {


    "sinBeta": 0.17364818,
    "sinAlphaT": 0.34666651,
    "sinAlphaWT": 0.36857144,
    "sinAlphaN": 0.34202014,


    "cosAlphaT": 0.93798845,
    "cosAlphaWT": 0.92959943,
    "cosAlphaN": 0.93969262,
    "cosBeta": 0.98480775,

    "tanBeta": 0.17632698,
    "tanAlphaT": 0.36958505,
    "tanAlphaWT": 0.39648415,
    "tanAlphaN": 0.36397023,

}

weirdConst = {


    "vTd" : 1.914034069035748,

    "kA": 1.25,
    "kV": 1.197640885892165,

    "kFalpha": 1.2459368176568582,
    "kHalpha": 1.122968408828429,

    "kHbeta": 1.5,
    "kFbeta": 0.7738745742607857,



    "Yepsy": 0.7805854196541574,
    "YBeta": 0.957393,

    "Yx": 1,
    "YF1": 3,
    "YF2": 2,

}

def arcDinte(modululNominal, xn1, xn2):

    tanAlphaN = calcAngles["tanAlphaN"]

    Sn1 = modululNominal*(pi/2 + 2*xn1*tanAlphaN)
    Sn2 = modululNominal*(pi/2 + 2*xn2*tanAlphaN)

    print(f"Sn1 = ", Sn1)
    print(f"Sn2 = ", Sn2)

def coardaDivizare(Sn1, Sn2):

    cosBeta = calcAngles["cosBeta"]

    d1 = calcValues["d1"]
    d2 = calcValues["d2"]

    noSn1 = Sn1 - (Sn1**3 * cosBeta**4/(6*d1**2))
    noSn2 = Sn2 - (Sn2**3 * cosBeta**4/(6*d2**2))

    print("!Sn1 = ", noSn1)
    print("!Sn2 = ", noSn2)

def coardaConst(Sn1, Sn2):

    cosAlphaN = calcAngles["cosAlphaN"]

    noScn1 = Sn1*cosAlphaN**2
    noScn2 = Sn2*cosAlphaN**2

    print("!Scn1 = ", noScn1)
    print("!Scn2 = ", noScn2)

def inaltimeCoardaDivizare(Sn1, Sn2):

    cosBeta = calcAngles["cosBeta"]

    d1 = calcValues["d1"]
    da1 = calcValues["da1def"]

    d2 = calcValues["d2"]
    da2 = calcValues["da2def"]

    han1 = (da1 - d1) / 2 + Sn1**2*cosBeta**2/(4*d1)
    han2 = (da2 - d2) / 2 + Sn2**2*cosBeta**2/(4*d2)

    print("!han1 = ", han1)
    print("!han2 = ", han2)

def inaltimeCoardaConst():

    mn = 4
    hoa = 1

    xn1 = calcValues["xn1"]
    xn2 = calcValues["xn2"]

    sinAlphaN = calcAngles["sinAlphaN"]
    cosAlphaN = calcAngles["cosAlphaN"]

    hcn1 = mn*(hoa-pi*sinAlphaN*cosAlphaN/4 + xn1*cosAlphaN**2)
    hcn2 = mn*(hoa-pi*sinAlphaN*cosAlphaN/4 + xn2*cosAlphaN**2)


    print("!hcn1 = ", hcn1)
    print("!hcn2 = ", hcn2)

def calculForte(MtPinion):

    d1 = calcValues["d1"]

    tanAlphaN = calcAngles["tanAlphaN"]
    tanBeta = calcAngles["tanBeta"]

    cosBeta = calcAngles["cosBeta"]
    cosAlphaN = calcAngles["cosAlphaN"]

    Ft = 2*MtPinion/d1

    print(f"Ft1 = ", Ft)
    print(f"Ft2 = ", Ft)

    Fr = Ft * tanAlphaN*1/cosBeta

    print(f"Fr1 = ", Fr)
    print(f"Fr2 = ", Fr)

    Fa = Ft*tanBeta

    print(f"Fa1 = ", Fa)
    print(f"Fa2 = ", Fa)

    Fn = m.sqrt(Ft**2 + Fr**2 + Fa**2)

    print(f"Fn = ", Fn)

def verifLaObo(Ft, modululNominal):

    kA = weirdConst["kA"]
    kV = weirdConst["kV"]

    kFalpha = weirdConst["kFalpha"]
    kFbeta = weirdConst["kFbeta"]

    b1 = calcValues["b1"]
    b2 = calcValues["b2"]

    Yepsy = weirdConst["Yepsy"]
    YF1 = weirdConst["YF1"]
    YF2 = weirdConst["YF2"]
    YBeta = weirdConst["YBeta"]

    tauF1 = YF1*Yepsy*YBeta*Ft*kA*kV*kFalpha*kFbeta/(b1*modululNominal)
    tauF2 = YF2*Yepsy*YBeta*Ft*kA*kV*kFalpha*kFbeta/(b2*modululNominal)

    print("tauF1 = ", tauF1)
    print("tauF2 = ", tauF2)

def verifPittin(Ft1):

    kA = weirdConst["kA"]
    kV = weirdConst["kV"]

    kFalpha = weirdConst["kFalpha"]
    kFbeta = weirdConst["kFbeta"]
    kHalpha = weirdConst["kHalpha"]
    kHbeta = weirdConst["kHbeta"]
    i12 = 5.6


    b1 = calcValues["b1"]
    b2 = calcValues["b2"]

    d1 = calcValues["d1"]
    epsyAlpha = calcValues["epsyAlpha"]
    epsyBeta = calcValues["epsyBeta"]

    cosBeta = calcAngles["cosBeta"]
    cosAlphaT = calcAngles["cosAlphaT"]
    tanAlphaWT = calcAngles["tanAlphaWT"]

    zH = 2*cosBeta/(cosAlphaT*m.sqrt(tanAlphaWT))
    zEpsy = m.sqrt(((4-epsyAlpha) *(1-epsyBeta)/3) + epsyBeta/epsyAlpha)
    zBeta = m.sqrt(cosBeta)
    zE = 189.8

    tauH = zE*zH*zEpsy*zBeta*m.sqrt(Ft1*kA*kV*kHalpha*kHbeta*(i12+1)/(b2*d1*i12))

    print("tauH = ", tauH)

def main():

    Sn1 = 7.5206840891795865
    Sn2 = 6.725773106859586
    Ft  = 7147.132849854733

    MtPinion = 261266

    arcDinte(4, calcValues["xn1"], calcValues["xn2"])
    coardaDivizare(Sn1, Sn2)
    coardaConst(Sn1, Sn2)
    inaltimeCoardaDivizare(Sn1, Sn2)
    inaltimeCoardaConst()
    calculForte(MtPinion)
    verifLaObo(Ft, MtPinion)
    verifPittin(Ft)



    return 0

main()
