# Ingredient Adjuster

# Original recipe for 48 cookies
SUGAR = 1.5
BUTTER = 1.0
FLOUR = 2.75

cookies = int(input("How many cookies do you want? "))

factor = cookies / 48

print("\nIngredients needed:")
print(f"Sugar: {SUGAR * factor:.1f} cups")
print(f"Butter: {BUTTER * factor:.1f} cups")
print(f"Flour: {FLOUR * factor:.1f} cups")