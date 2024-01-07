try:from perlin_noise import PerlinNoise
except: 
	print("Error: install perlin noise for python with 'pip install perlin-noise'")
	exit(1)
import matplotlib.pyplot as plt
import json

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

xpix, ypix = 400, 400
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/100, j/100])
        noise_val += 0.5 * noise2([i/100, j/100])
        noise_val += 0.25 * noise3([i/100, j/100])
        noise_val += 0.125 * noise4([i/100, j/100])

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='gray')
f = open("perlin.json", "w")
f.write(json.dumps(pic))
f.close()
plt.show()