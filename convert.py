# File: convert.py
# A simple program that converts celsius to Fahrenheit

def main():
    print("This is a program specifically for", end=" ")
    print("calculating temperature in Fahrenheit", end=" ")
    print("from Celcius :-)")

    #print("Celsius", "Fahrenheit")
    for temp_cels in range(0,100,10):
       #temp_cels = eval(input("Please input the temperature to be converted: "))
        temp_fahr = (9/5 * temp_cels) + 32
        print("Celsius", "Fahrenheit")
        print(temp_cels, temp_fahr)

main()