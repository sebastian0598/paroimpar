numero= int(input("digite un numero: "))
def numero_par_o_impar():
    if numero%2==0:
        print(f"el numero: {numero} es par")
    else:
         print(f"el numero: {numero}  es impar")    
    return (numero)
    

def main():
    numero_par_o_impar()

if __name__ == "__main__":
    main()