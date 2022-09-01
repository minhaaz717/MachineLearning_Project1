lbs =  [150, 155, 145, 148, 120, 130, 100]
kgs = []

#converting weight from lbs to kgs
for i in lbs:
    kgs.append(round(i * 0.45359237,2))

print(f"weight conversion in kgs: {kgs}")