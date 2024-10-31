import math
import random
import gmpy2
import requests
from functools import reduce
import time
from factordb.factordb import FactorDB


def findPQFromN(n, input):
    pq = n // input
    return pq


def findNFromPQ(p, q):
    n = p * q
    return n


def findPQFromPhi(input, phi):
    pq = (phi / (input - 1)) + 1
    return pq


def findPTFromCTDN(ct, d, n):
    pt = pow(ct, d, n)
    return pt


def findPhiFromPQ(p, q):
    if p == q:
        phi = p * (p - 1)
    else:
        phi = (p - 1) * (q - 1)
    return phi


def findCTFromPTEN(pt, e, n):
    ct = pow(pt, e, n)
    return ct


def findDFromEPhi(e, phi):
    d = getModularInverse(e, phi)
    return d


def findEfromPhi(phi):
    g = 0
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)
    return e


def findIfOptionInInputs(option, inputs):
    for input in inputs:
        if option in input:
            return 1
    return 0


def getValueOptionFromInputs(option, inputs):
    for input in inputs:
        if option in input:
            if option == "CT":
                return input[1]
            else:
                return gmpy2.mpz(input[1])


def convertNumberToBytes(number):
    textString = number.to_bytes((number.bit_length() + 7) // 8, 'big')
    return textString


def convertBytesToNumber(bytes):
    bytesArray = str.encode(bytes)
    numberString = int.from_bytes(bytesArray, 'big')
    return numberString


def getModularInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def checkAllInputsValid(inputs):
    for inputNumber in range(len(inputs)):
        if inputs[inputNumber][0] == "PT":
            try:
                intInput = gmpy2.mpz(inputs[inputNumber][1])
            except:
                inputs[inputNumber][1] = str(convertBytesToNumber(inputs[inputNumber][1]))
        elif inputs[inputNumber][0] == "CT":
            if "," in inputs[inputNumber][1]:
                ct = inputs[inputNumber][1].split(",")
                for c in range(len(ct)):
                    try:
                        ct[c] = gmpy2.mpz(ct[c])
                    except:
                        return False
                inputs[inputNumber][1] = ct
            else:
                ct = []
                ct.append(gmpy2.mpz(inputs[inputNumber][1]))
                inputs[inputNumber][1] = ct

        else:
            try:
                intInput = gmpy2.mpz(inputs[inputNumber][1])
            except:
                return False
    return RSAToolInputs


def findFactorsFromN(n):
    if len(str(n)) >= 77:
        print("[*] The N supplied is very large. Factorization may take a while!")
    print("[*] Trying to factorize N. Please wait...")
    factors = []
    counter = 0
    response = requests.get("http://factordb.com/api", params={"query": str(n)}).json()
    status = response.get('status')
    factorsList = response.get('factors')
    for factor in factorsList:
        if factor[0] != n:
            factors.append(factor[0])
    while status != 'FF':
        time.sleep(15)
        f = FactorDB(n)
        f.connect()
        factors = f.get_factor_list()
        status = f.get_status()
        if (counter % 2) == 0:
            print("[*] Still trying to factorize N. Please wait...")
        counter += 1
    for factor in range(len(factors)):
        factors[factor] = int(factors[factor])
    print("[*] Successfully factored N!\n")
    return factors


RSAToolOptions = ["P", "Q", "N", "PHI", "E", "D", "CT", "PT"]
RSAToolOutputValue = 0
print("[*] Welcome to the RSA CTF Tool!")
RSAToolOutput = input("[?] What would you like to find? (Options are P, Q, N, PHI, E, D, CT, PT) : ").upper()
while RSAToolOutput not in RSAToolOptions:
    RSAToolOutput = input("[!] Invalid choice. Please try again: ").upper()

RSAToolOptions.remove(RSAToolOutput)

while True:
    RSAToolInputs = []
    print("\n[*] What inputs have you got? (Leave blank as appropriate)")
    for optionNumber in range(len(RSAToolOptions)):
        optionChoice = input("[?] " + RSAToolOptions[optionNumber] + ": ")
        if optionChoice != "":
            RSAToolInputs.append([RSAToolOptions[optionNumber], optionChoice])
    validInputs = checkAllInputsValid(RSAToolInputs)
    if validInputs == False:
        print("[!] Inputs are invalid. Please try again.")
    else:
        RSAToolInputs = validInputs
        break

print("\n[*] Processing based on inputs...\n")

if RSAToolOutput in ["P", "Q"] and findIfOptionInInputs("N", RSAToolInputs) and (
        findIfOptionInInputs("P", RSAToolInputs) or findIfOptionInInputs("Q", RSAToolInputs)):
    n = getValueOptionFromInputs("N", RSAToolInputs)
    if findIfOptionInInputs("P", RSAToolInputs):
        p = getValueOptionFromInputs("P", RSAToolInputs)
        q = findPQFromN(n, p)
        RSAToolOutputValue = q
    elif findIfOptionInInputs("Q", RSAToolInputs):
        q = getValueOptionFromInputs("Q", RSAToolInputs)
        p = findPQFromN(n, q)
        RSAToolOutputValue = p

elif "N" in RSAToolOutput and findIfOptionInInputs("P", RSAToolInputs) and findIfOptionInInputs("Q", RSAToolInputs):
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    n = findNFromPQ(p, q)
    RSAToolOutputValue = n

elif "P" in RSAToolOutput and findIfOptionInInputs("PHI", RSAToolInputs) and (
        findIfOptionInInputs("P", RSAToolInputs) or findIfOptionInInputs("Q", RSAToolInputs)):
    phi = getValueOptionFromInputs("PHI", RSAToolInputs)
    if findIfOptionInInputs("P", RSAToolInputs):
        p = getValueOptionFromInputs("P", RSAToolInputs)
        q = findPQFromPhi(p, phi)
        RSAToolOutputValue = q
    elif findIfOptionInInputs("Q", RSAToolInputs):
        q = getValueOptionFromInputs("Q", RSAToolInputs)
        p = findPQFromPhi(q, phi)
        RSAToolOutputValue = p

elif "N" in RSAToolOutput and findIfOptionInInputs("PHI", RSAToolInputs) and (
        findIfOptionInInputs("P", RSAToolInputs) or findIfOptionInInputs("Q", RSAToolInputs)):
    phi = getValueOptionFromInputs("PHI", RSAToolInputs)
    if findIfOptionInInputs("P", RSAToolInputs):
        p = getValueOptionFromInputs("P", RSAToolInputs)
        q = findPQFromPhi(p, phi)
    elif findIfOptionInInputs("Q", RSAToolInputs):
        q = getValueOptionFromInputs("Q", RSAToolInputs)
        p = findPQFromPhi(q, phi)
    n = findNFromPQ(p, q)
    RSAToolOutputValue = n

elif "PHI" in RSAToolOutput and findIfOptionInInputs("P", RSAToolInputs) and findIfOptionInInputs("Q", RSAToolInputs):
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    phi = findPhiFromPQ(p, q)
    RSAToolOutputValue = phi

elif "PHI" in RSAToolOutput and findIfOptionInInputs("N", RSAToolInputs) and (
        findIfOptionInInputs("P", RSAToolInputs) or findIfOptionInInputs("Q", RSAToolInputs)):
    n = getValueOptionFromInputs("N", RSAToolInputs)
    if findIfOptionInInputs("P", RSAToolInputs):
        p = getValueOptionFromInputs("P", RSAToolInputs)
        q = findPQFromN(n, p)
    elif findIfOptionInInputs("Q", RSAToolInputs):
        q = getValueOptionFromInputs("Q", RSAToolInputs)
        p = findPQFromN(n, q)
    phi = findPhiFromPQ(p, q)
    RSAToolOutputValue = phi

elif "E" in RSAToolOutput and findIfOptionInInputs("N", RSAToolInputs) and not findIfOptionInInputs("P",
                                                                                                    RSAToolInputs) and not findIfOptionInInputs(
        "Q", RSAToolInputs):
    n = getValueOptionFromInputs("N", RSAToolInputs)
    factors = findFactorsFromN(n)
    if len(factors) == 2:
        p = factors[0]
        q = factors[1]
        phi = findPhiFromPQ(p, q)
        e = findEfromPhi(phi)
        RSAToolOutputValue = e
    else:
        print("[!] Too many factors from n! Could not find a P and Q.")

elif "D" in RSAToolOutput and findIfOptionInInputs("E", RSAToolInputs) and findIfOptionInInputs("PHI", RSAToolInputs):
    e = getValueOptionFromInputs("E", RSAToolInputs)
    phi = getValueOptionFromInputs("PHI", RSAToolInputs)
    d = findDFromEPhi(e, phi)
    RSAToolOutputValue = d

elif "D" in RSAToolOutput and findIfOptionInInputs("E", RSAToolInputs) and findIfOptionInInputs("P",
                                                                                                RSAToolInputs) and findIfOptionInInputs(
        "Q", RSAToolInputs):
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    e = getValueOptionFromInputs("E", RSAToolInputs)
    phi = findPhiFromPQ(p, q)
    d = findDFromEPhi(e, phi)
    RSAToolOutputValue = d

elif "PT" in RSAToolOutput and findIfOptionInInputs("CT", RSAToolInputs) and findIfOptionInInputs("D",
                                                                                                  RSAToolInputs) and findIfOptionInInputs(
        "N", RSAToolInputs):
    ct = getValueOptionFromInputs("CT", RSAToolInputs)
    d = getValueOptionFromInputs("D", RSAToolInputs)
    n = getValueOptionFromInputs("N", RSAToolInputs)
    pt = []
    for cipher in ct:
        pta = findPTFromCTDN(cipher, d, n)
        pt.append(pta)
    RSAToolOutputValue = pt

elif "PT" in RSAToolOutput and findIfOptionInInputs("CT", RSAToolInputs) and findIfOptionInInputs("D",
                                                                                                  RSAToolInputs) and findIfOptionInInputs(
        "P", RSAToolInputs) and findIfOptionInInputs("Q", RSAToolInputs):
    ct = getValueOptionFromInputs("CT", RSAToolInputs)
    pt = []
    d = getValueOptionFromInputs("D", RSAToolInputs)
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    n = findNFromPQ(p, q)
    for cipher in ct:
        pta = findPTFromCTDN(cipher, d, n)
        pt.append(pta)
    RSAToolOutputValue = pt

elif "PT" in RSAToolOutput and findIfOptionInInputs("E", RSAToolInputs) and findIfOptionInInputs("Phi",
                                                                                                 RSAToolInputs) and (
        findIfOptionInInputs("P", RSAToolInputs) or findIfOptionInInputs("Q", RSAToolInputs)) and findIfOptionInInputs(
        "CT", RSAToolInputs):
    ct = getValueOptionFromInputs("CT", RSAToolInputs)
    e = getValueOptionFromInputs("E", RSAToolInputs)
    phi = getValueOptionFromInputs("PHI", RSAToolInputs)
    if findIfOptionInInputs("P", RSAToolInputs):
        p = getValueOptionFromInputs("P", RSAToolInputs)
        q = findPQFromPhi(p, phi)
    if findIfOptionInInputs("Q", RSAToolInputs):
        q = getValueOptionFromInputs("Q", RSAToolInputs)
        p = findPQFromPhi(q, phi)
    n = findNFromPQ(p, q)
    d = findDFromEPhi(e, phi)
    pt = []
    for cipher in ct:
        pta = findPTFromCTDN(cipher, d, n)
        pt.append(pta)
    RSAToolOutputValue = pt

elif "PT" in RSAToolOutput and findIfOptionInInputs("CT", RSAToolInputs) and findIfOptionInInputs("E",
                                                                                                  RSAToolInputs) and findIfOptionInInputs(
        "P", RSAToolInputs) and findIfOptionInInputs("Q", RSAToolInputs):
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    ct = getValueOptionFromInputs("CT", RSAToolInputs)
    e = getValueOptionFromInputs("E", RSAToolInputs)
    n = findNFromPQ(p, q)
    phi = findPhiFromPQ(p, q)
    d = findDFromEPhi(e, phi)
    pt = []
    for cipher in ct:
        pta = findPTFromCTDN(cipher, d, n)
        pt.append(pta)
    RSAToolOutputValue = pt

elif "PT" in RSAToolOutput and findIfOptionInInputs("N", RSAToolInputs) and findIfOptionInInputs("E",
                                                                                                 RSAToolInputs) and findIfOptionInInputs(
        "CT", RSAToolInputs):
    tryOther = True
    n = getValueOptionFromInputs("N", RSAToolInputs)
    e = getValueOptionFromInputs("E", RSAToolInputs)
    ct = getValueOptionFromInputs("CT", RSAToolInputs)
    pt = []
    response = requests.get("http://factordb.com/api", params={"query": str(n)}).json()
    status = response.get('status')
    if status == 'P':
        phi = n - 1
        d = findDFromEPhi(e, phi)
        for cipher in ct:
            pta = findPTFromCTDN(cipher, d, n)
            pt.append(pta)
        RSAToolOutputValue = pt
        tryOther = False
    elif (n / e) > 100000 and e < 100:
        for cipher in ct:
            pta, exact = gmpy2.iroot(cipher, e)
            pt.append(pta)
        RSAToolOutputValue = pt
        try:
            for plain in RSAToolOutputValue:
                RSAToolOutputValue = convertNumberToBytes(int(RSAToolOutputValue)).decode()
                tryOther = False
        except:
            pass
    if tryOther == True:
        factors = findFactorsFromN(n)
        if len(factors) == 1:
            phi = factors[0] * (factors[0] - 1)
        elif n == reduce(lambda x, y: x * y, factors):
            phi = 1
            for factor in factors:
                phi *= factor - 1
        d = findDFromEPhi(e, phi)
        for cipher in ct:
            pta = findPTFromCTDN(cipher, d, n)
            pt.append(pta)
        RSAToolOutputValue = pt
        print("[*] FACTORS: ", factors)
        print("[*] PHI: ", phi)
        print("[*] D: ", d)

elif "CT" in RSAToolOutput and findIfOptionInInputs("P", RSAToolInputs) and findIfOptionInInputs("Q",
                                                                                                 RSAToolInputs) and findIfOptionInInputs(
        "E", RSAToolInputs) and findIfOptionInInputs("PT", RSAToolInputs):
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    pt = getValueOptionFromInputs("PT", RSAToolInputs)
    e = getValueOptionFromInputs("E", RSAToolInputs)
    n = findNFromPQ(p, q)
    ct = findCTFromPTEN(pt, e, n)
    RSAToolOutputValue = ct

elif "CT" in RSAToolOutput and findIfOptionInInputs("N", RSAToolInputs) and findIfOptionInInputs("E",
                                                                                                 RSAToolInputs) and findIfOptionInInputs(
        "PT", RSAToolInputs):
    pt = getValueOptionFromInputs("PT", RSAToolInputs)
    e = getValueOptionFromInputs("E", RSAToolInputs)
    n = getValueOptionFromInputs("N", RSAToolInputs)
    ct = findCTFromPTEN(pt, e, n)
    RSAToolOutputValue = ct

elif "CT" in RSAToolOutput and findIfOptionInInputs("N", RSAToolInputs) and findIfOptionInInputs("PT", RSAToolInputs):
    n = getValueOptionFromInputs("N", RSAToolInputs)
    pt = getValueOptionFromInputs("PT", RSAToolInputs)
    factors = findFactorsFromN(n)
    if len(factors) == 2:
        p = factors[0]
        q = factors[1]
        phi = findPhiFromPQ(p, q)
        e = findEfromPhi(phi)
        ct = findCTFromPTEN(pt, e, n)
        RSAToolOutputValue = ct
    else:
        print("[!] Too many factors from n! Could not find a P and Q.")


elif "E" in RSAToolOutput and findIfOptionInInputs("P", RSAToolInputs) and findIfOptionInInputs("Q", RSAToolInputs):
    p = getValueOptionFromInputs("P", RSAToolInputs)
    q = getValueOptionFromInputs("Q", RSAToolInputs)
    phi = findPhiFromPQ(p, q)
    e = findEfromPhi(phi)
    RSAToolOutputValue = e

elif RSAToolOutput in ["P", "Q"] and findIfOptionInInputs("N", RSAToolInputs) and (
        not findIfOptionInInputs("Q", RSAToolInputs) or not findIfOptionInInputs("P", RSAToolInputs)):
    n = getValueOptionFromInputs("N", RSAToolInputs)
    factors = findFactorsFromN(n)
    if len(factors) == 2:
        p = factors[0]
        q = factors[1]
        RSAToolOutputValue = (p, q)
    else:
        print("[!] Too many factors from n! Could not find a P and Q.")

if RSAToolOutput in ["P", "Q"] and type(RSAToolOutputValue) is tuple:
    p = RSAToolOutputValue[0]
    q = RSAToolOutputValue[1]
    print("[*] P is: " + str(p))
    print("[*] Q is: " + str(q))
elif "PT" in RSAToolOutput:
    for pta in range(len(pt)):
        pt[pta] = str(pt[pta])
    pt = ''.join(RSAToolOutputValue)
    print("[*] " + RSAToolOutput + " is: " + str(pt))
    userChoice = input("[?] Would you like to convert your numeric plaintext to ascii? (Y/N): ").upper()
    while userChoice not in ["Y", "N"]:
        userChoice = input("[!] That's not a valid choice. Please try again: ").upper()
    if userChoice == "Y":
        for outputValue in range(len(RSAToolOutputValue)):
            try:
                RSAToolOutputValue[outputValue] = str(convertNumberToBytes(int(RSAToolOutputValue[outputValue])).decode())
            except:
                pass
        pt = ''.join(RSAToolOutputValue)
        print("[*] " + RSAToolOutput + " is: " + str(pt))
elif type(RSAToolOutputValue) is not tuple:
    RSAToolOutputValue = int(RSAToolOutputValue)
    if RSAToolOutputValue != 0:
        print("[*] " + RSAToolOutput + " is: " + str(RSAToolOutputValue))
    else:
        print("[!] Couldn't decode with the specified inputs. Try with a different combination...")
