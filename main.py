## Author Shubhang Srikoti svs6959@psu.edu
## Collaborator Zihan Xia zfx5078@psu.edu
## Collaborator Xinyi Yang xvy5166@psu.edu
## Collaborator Lynn Francis jtf5383@psu.edu
temp = float(input("Enter temperature: "))

##unit = input("Enter unit in F/f or C/c: ")
##if unit == "F" or unit == "f":
  ##print ("Converting Fahrenheit to Celsius.")
  ##fahrenheit1 = float(fahrenheit1)
  ##celsius2 = ((fahrenheit1 - 32) * 5/9)
  ##celsius2 = str(celsius2)
  ##print(str(farenheit1) + "° in Fahrenheit is equivalent to " + str(celsius2) + "° in Celsius.")
## if unit == "C" or unit == "c":
  ##print ("Converting Celsius to Fahrenheit.")
  ##celsius1 = float(celsius1)
  ##fahrenheit2 = ((celsius1 * 9) / 5 + 32)
  ##fahrenheit2 = str(fahrenheit2)
  ##print (str(celsius1) + "° in Celsius is equivalent to " + str(fahrenheit2) + "° in Fahrenheit")

unit = str(input("Enter unit in F/f or C/c: "))
if unit == "F" or unit == "f":
  print("Converting Fahrenheit to Celsius.")
  newCelsius = (temp - 32) * 5/9
  print(f"{temp}° in Fahrenheit is equivalent to {newCelsius}° in Celsius.")
elif unit == "C" or unit == "c":
  print("Converting Celsius to Fahrenheit.")
  newFahrenheit = (temp * 9/5) - 32
  print(f"{temp}° in Celsius is equivalent to {newFahrenheit}° Fahrenheit.")