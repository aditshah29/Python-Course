#String Formatting

template="Dear {}, you are great. Take this {}$ bag."

a="John"
a1=10000

s1=template.format(a,a1)
print(s1)

print(f"{a}, you are awesome. Take this {a1}$ bag.")