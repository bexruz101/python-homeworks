txt = "LMaasleitbtui"

cars = ["Malibu", "Lasetti"]
extracted_cars = []


for i in cars:
    string = ""
    for j in i:
        if j in txt:
            string += j
    if string != "":
        extracted_cars.append(string)

print(extracted_cars)
