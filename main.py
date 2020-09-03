## Author Shubhang Srikoti svs6959@psu.edu
## Collaborator Zihan Xia zfx5078@psu.edu
## Collaborator Xinyi Yang xvy5166@psu.edu
## Collaborator Lynn Francis jtf5383@psu.edu
temp = float(input("Enter temperature: "))


unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  ##print("Converting Fahrenheit to Celsius.")
  newCelsius = ((temp - 32) * 5)/9
  print(f"{temp}° in Fahrenheit is equivalent to {newCelsius}° Celsius.")
elif unit == "C" or unit == "c":
  ##print("Converting Celsius to Fahrenheit.")
  newFahrenheit = (temp * 1.8) + 32
  print(f"{temp}° in Celsius is equivalent to {newFahrenheit}° Fahrenheit.")