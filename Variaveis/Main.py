def main():
    email = input ("digite o email do paciente ")
    idade = int (input ("digite a idade do paciente: "))
    altura = float (input("digite a altura do paciente; "))
    isSaudavel = input("ele está saudavel ")

    print("email do paciente", email, "a sua idade e", idade ,"e sua ", altura)

    if isSaudavel=="sim"or isSaudavel == "S":
        print("o paciente está saudavel")
    elif isSaudavel == "está":
        print("ele está saudavel")
    else:
        print;("o paciente não está saudavel")

    return 0
main()