plants = []  # список для збереження назв рослин

print("Гра 'Рослинництво'")
print("Введіть назви рослин. Щоб завершити напишіть 'стоп'.")

while True:
    plant = input("Введіть рослину: ")
    if plant.lower() == "стоп":
        break
    plants.append(plant)

print("\nВаші рослини у грі:")
for p in plants:
    print("🌱", p)
