#Smart Temperature Converter 
#Take input in Celsius and print its equivalent in Fahrenheit and Kelvin. 
#(Use explicit type conversion and arithmetic operators.)

#● Fahrenheit = (C × 9/5) + 32 
#● Kelvin = C + 273.15 

celcius = float(input("Enter the temperature in Celcius: ")) # take input in int type value
fahrenheit = float((celcius * 9/5) + 32) # here float use as a Explicit type conversion
kelvin = celcius + 273.15
print("Temperature in Fahrenheit is:",fahrenheit,"F")
print("Temperaure in Kelvin is:",kelvin,"K")