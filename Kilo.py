height = input()

weight = input()

height_float = float(height)

weight_int = int(weight)
# burada height'i başa alırsak cevap 0'lı çıkıyor o yüzden weight'i öne almalıyız.
bmi = weight_int / height_float ** 2

bmi_int = int(bmi)

print(bmi_int)