import numpy as np

array = open("input.txt").read().strip()
array = np.array(list(map(int, array)))

wide, tall = 25, 6
size = int(len(array) / wide / tall)

images = array.reshape((size, tall, wide))

def count(arr):
    unique, counts = np.unique(arr, return_counts=True)
    return dict(zip(unique, counts))

arbitary_max = 1000
min_0 = arbitary_max
min_image = None
min_image_counter = None
for image in images:
    counter = count(image)
    now_0 = counter.get(0, arbitary_max)
    if now_0 < min_0:
        min_0 = now_0
        min_image = image
        min_image_counter = counter
print(min_image_counter[1] * min_image_counter[2])


############### 
# part2
#a, tall, wide = np.array(list(map(int, "0222112222120000"))), 2, 2
#images = a.reshape((4, tall, wide,))
final = np.zeros((tall, wide), dtype=int)
final.fill(-1)
for image in images:
    for y in range(tall):
        for x in range(wide):
            if final[y][x] == -1:
                if image[y][x] == 2:
                    pass
                elif image[y][x] == 1:
                    final[y][x] = image[y][x]
                elif image[y][x] == 0:
                    final[y][x] = image[y][x]

top_left = final[0][0]
top_right = final[0][-1]
bottom_left = final[-1][0]
bottom_right = final[-1][-1]
print(final)

# Imaging
from PIL import Image  # pip install pillow

data = np.zeros((tall, wide), dtype=np.uint8)
for y in range(tall):
    for x in range(wide):
        data[y][x] = 128 if final[y][x] else 0
img = Image.fromarray(data, 'L')
img.save('final.png')
img.show()
