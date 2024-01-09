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

xpix, ypix = 5000, 50
scale = 25
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/scale, j/scale])
        noise_val += 0.5 * noise2([i/scale, j/scale])
        noise_val += 0.25 * noise3([i/scale, j/scale])
        noise_val += 0.125 * noise4([i/scale, j/scale])

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='gray')
f = open("perlin.json", "w")
f.write(json.dumps(pic))
f.close()
f = open("perlin.csv", "w")
f.write(",".join((str(c) for c in range(ypix)))+"\n")
f.write("\n".join((",".join((str(c) for c in r)) for r in pic)))
f.close()
plt.show()