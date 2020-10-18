from PIL import Image
from os import listdir

def split_cr(im,c,r,sep=False):
  #print(im.format, im.size, im.mode)
  w = im.size[0]//c
  h = im.size[1]//r
  if sep:
    wl = w+1
    hl = h+1
  else:
    wl = w
    hl = h
  output = []
  for y in range(0,im.size[1],hl):
    for x in range(0,im.size[0],wl):
      #print(x,y,w,h)
      cropped = im.crop((x, y, x + w, y + h))
      output.append(cropped)
  return output

def split_wh(im,w,h,sep=False):
  #print(im.format, im.size, im.mode)
  output = []
  if sep:
    wl = w+1
    hl = h+1
  else:
    wl = w
    hl = h
  for y in range(0,im.size[1],hl):
    for x in range(0,im.size[0],wl):
     # print(x,y,w,h)
      cropped = im.crop((x, y, x + w, y + h))
      output.append(cropped)
  return output

def merge_cr(in_array,c,r):
  w = in_array[0].size[0]
  h = in_array[0].size[1]
  output = Image.new("RGBA", (w * c, h * r), 0)
  count = 0
  for y in range(0,output.size[1],h):
    for x in range(0,output.size[0],w):
      if count < len(in_array):
        print(count,x,y,w,h)
        output.paste(in_array[count],(x, y))
      count += 1
  return output

def merge_auto(in_array):
  w = in_array[0][0].size[0]
  h = in_array[0][0].size[1]
  output = Image.new("RGBA", (w * len(in_array), h * len(in_array[0])), 0)
  for y in range(0,output.size[1],h):
    for x in range(0,output.size[0],w):
      print(x,y,w,h)
      output.paste(in_array[x//w][y//h],(x, y))
  return output

def merge_dir_cr(in_dir,c,r):
  in_array = []
  file_list = listdir(in_dir)
  file_list.sort()
  for in_file_name in file_list:
    in_file = in_dir + in_file_name
    in_array.append(Image.open(in_file))
  output = merge_cr(in_array,c,r)
  return output

def split_to_dir_cr(in_file_path,c,r,output_dir):
  im = Image.open(in_file_path)
  outputs = split_cr(im,c,r)
  count=0
  for output in outputs:
    count += 1
    output.save(output_dir + str(count)+".png")

def split_to_dir_wh(in_file_path,w,h,output_dir):
  im = Image.open(in_file_path)
  outputs = split_wh(im,w,h)
  count=0
  for output in outputs:
    count += 1
    output.save(output_dir + str(count)+".png")

def transform_autotile(im):
  tilemap = {
    #0: [0, 8, 110, 162, 160],
    8: [0, 8, 110, 162, 160],
    9: [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 34, 35, 163, 174],
    #1: [7, 15, 111, 175, 161],
    11: [7, 15, 111, 175, 161],
    12: [16, 24, 32, 46, 48, 62, 64, 78, 80, 96, 102, 112, 118, 126, 128, 168],
    7: [17, 29, 49, 51, 53, 83, 85, 89, 91, 113, 115, 151, 157],
    21: [18, 19, 145, 146, 147, 158, 179, 180, 181, 182, 185, 186, 187, 188, 189, 190],
    6: [20, 30, 50, 52, 54, 84, 86, 90, 92, 114, 116, 148, 152],
    13: [21, 22, 25, 26, 27, 28, 37, 38, 41, 42, 43, 44, 55, 56, 57, 58, 59, 60, 71, 72, 73, 74, 75, 76, 81, 82, 87, 88, 97, 98, 103, 104, 119, 120, 121, 122, 123, 124, 135, 136, 137, 138, 139, 140, 149, 150, 153, 154, 155, 156, 165, 166, 169, 170, 171, 172],
    15: [23, 31, 45, 47, 61, 63, 77, 79, 93, 101, 109, 117, 125, 127, 143, 167],
    3: [33, 39, 65, 67, 69, 99, 105, 107, 129, 131, 133, 141, 173],
    2: [36, 40, 66, 68, 70, 100, 106, 108, 130, 132, 134,142, 164],
    #4: [94, 144, 178, 184,  176],
    20: [94, 144, 178, 184,  176],
    #5: [95, 159, 183, 191,  177]
    23: [95, 159, 183, 191,  177]
    #160: [160, 161, 176, 177]
  }
  base_tiles = split_cr(im,4,6)
  finals = [Image.new("RGBA",(base_tiles[0].size[0],base_tiles[0].size[1]),1)] * 192
  for tile in tilemap:
    base_tile = base_tiles[tile]
    for dest in tilemap[tile]:
      finals[dest] = base_tile
  return merge_cr(finals,16,12)

def transform_a4_wall(im):
  crops = [
    (0,0,16,32),
    (8,0,24,32),
    (16,0,32,32)
  ]
  in_array = []
  for croper in crops:
    in_array.append(im.crop(croper))
  return merge_cr(in_array,3,1)

def get_tilemap(im):
  basetiles = {}
  tilemap = {}
  in_array = []
 # subtiles = split_cr(im,16,12)
  subtiles = split_wh(im,16,16,True)
  #subtiles = split_cr(im,4,6)
  index = 0
  for tile in subtiles:
    found = False
    for basetile in basetiles:
      if list(basetiles[basetile].getdata()) == list(tile.getdata()):
        found = True
        tilemap[basetile].append(index)
        break
    if not found:
      basetiles[index] = tile
      tilemap[index] = []
      tilemap[index].append(index)
    index += 1
  return (basetiles,tilemap)

def save_arr_to_dir(in_array, dir_path):
  count = 0
  for im in in_array:
    count += 1
    im.save(dir_path + str(count) + ".png")

def save_dict_to_dir(dict, dir_path):
  for im in dict:
    dict[im].save(dir_path + str(im) + ".png")
