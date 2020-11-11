##################
# Ley de la suma #
#################
def f(n):
    
    for i in range(n):
        
        print(i)
        
    for i in range(n):
        print(i)

# O(n) + O(n) = O( n + n ) = O(2n) = O(n)

#Solo importa el termino más grande

def f(n):
    
    for i in range(n):
        
        print(i)
        
    for i in range( n * n ):
        
        print(i)
        
# O(n) + O( n * n ) = O(n + n^2) = O(n^2)

#############################
# Ley de la multiplicación #
############################

def f(n):
    
    for i in range(n):
        
        for j in range(n):
            
            print(i,j)

# O(n) * O(n) = O(n * n) = O(n^2)

##########################
# Recursividad multiple #
#########################

def fibonacci(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 1)

# O(2**n)

# Loop = crecimiento lineal
# Loop dentro de Loop = crecimiento cuadratico
# Llamadas recursivas = crecimiento exponencial