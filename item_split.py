import omega_helper
from PIL import Image
from os import listdir

im = Image.open("input/character5_5.png")
a = omega_helper.split_cr(im,3,4)
b = []
for i in range(4):
  b.append([])
  for j in range(3):
    print(i,j)
    b[i].append(a[i*3 + j])
print(len(b))
omega_helper.merge_auto(b).save("output/character5_5.png")


