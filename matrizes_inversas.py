import numpy as np

from fractions import Fraction
# Se tem em uma equação com expoente negativo,
# a elevado por -1 se tem 1/a, a * a elevado por -1, tem se como operação a/a, resultando assim 1

# a = 10
# print(a * (a ** -1)) # 1

# Então quando se tem uma matriz invertivel, se tem a seguinte operação A * (A elevado a -1)
result_A = [[1,0], [0,1]] # result A = A *(A elevado a -1)
# sendo que A elevado por menos 1 = 1/det(A) * [[d -b], [-c a]], com essa formula vc multiplica por A
# Se A é 
A = np.array([[6,1], [5,2]])
# Invertida de A é
AInvertida = np.array([[2,-1], [-5,6]])
# Det de A é
detA = np.linalg.det(A) # 7
# Intertida do Det(A) é
detAInvertida = detA ** -1 # 1/7
# Mult de Det(A**-1) * AIntertida é
detAMult = np.dot(detAInvertida, AInvertida) #
# Mult de A * (A**-1) É
AVezesA = np.dot(A,detAMult) #

# Convertendo os resultados para frações
detA_fraction = Fraction(detA).limit_denominator()
detAInvertida_fraction = Fraction(detAInvertida).limit_denominator()
detAMult_fraction = np.array([[Fraction(x).limit_denominator() for x in row] for row in detAMult])
AVezesA_fraction = np.array([[Fraction(x).limit_denominator() for x in row] for row in AVezesA])



print("Det(A) = \n", detA_fraction)
print("-" * 30)
print("Det(A**-1) = \n", detAInvertida_fraction)
print("-" * 30)
print("Det(A**-1) * AInvertida = \n", detAMult_fraction)
print("-" * 30)
print("A * (A ** -1) = \n", AVezesA_fraction)