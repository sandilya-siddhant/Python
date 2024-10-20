def Mathematical_Operation(Number01, Number02, operation) :
    if operation == 'add':
        return Number01 + Number02
    elif operation == 'subtract' :
        return Number01 - Number02
    elif operation == 'multiply' :
        return Number01 * Number02
    elif operation == 'divide' :
        return Number01 / Number02
    else :
        return "Error - Invalid Operation"
Number01=int(input("Write 1st No. :"))
Number02=int(input("Write 2nd No. :"))
operation=input("Which operation you want to use add , subtract , multiply , divide : ")

result=Mathematical_Operation(Number01, Number02, operation)
print("The Result is:",result)
