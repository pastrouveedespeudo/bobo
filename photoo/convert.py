from PIL import Image




path = r"C:\Users\jeanbaptiste\bobo\bobo\static\img\portfolio\coupe\coucou.png"
img = Image.open(path).convert("LA")
img.save("1.2.png")
