[CSAW '23] 1black0white
Converting Binary Data into a QR code.
Distribution
We were provided a data file with some decimal data.
<pre>
533258111
274428993
391005533
391777629
390435677
273999169
534074751
99072
528317354
446173689
485174588
490627992
105525542
421383123
132446300
431853817
534345998
496243321
365115424
302404521
289808374
1437979
534308692
272742168
391735804
391385911
391848254
273838450
534645340
</pre>
# Solution
Based on the challenge title, I knew I wanted to use the data to visualize a QR code, where 
1
1
 is black and 
0
0
 is white. There were some initial issues with this approach:
The data was in decimal, not binary
Not all the lines were the same length.
We can fix this by converting the data to binary and then padding the lines until they are all the same length. It turns out the longest line is 
29
29
 binary digits long so we can pad to this length.
<pre>
data = open('data.txt').read().strip().split()
binary = ''.join(bin(int(num))[2:].zfill(29) for num in data)
</pre>
Now, we can use PIL (the Python Imaging Library) to create an image from the binary data. I made a new image and then looped through the binary data, setting each pixel to black or white based on the value of the binary digit.
<pre>
index = 0
for x in range(size):
    for y in range(size):
        if index < len(binary):
            pixels[x, y] = int(binary[index])
            index += 1
            </pre>
To ensure my phone could scan the image, I resized it to be 
10
10
 times the original size.
large = img.resize((10 * size, 10 * size))
large.show()
This generates an image that gives us the flag when we scan it.
Full Solution
<pre>
from PIL import Image
​
data = open('data.txt').read().strip().split()
binary = ''.join(bin(int(num))[2:].zfill(29) for num in data)
​
size = int(len(binary) ** 0.5)
img = Image.new('1', (size, size))
pixels = img.load()
​
index = 0
for x in range(size):
    for y in range(size):
        if index < len(binary):
            pixels[x, y] = int(binary[index])
            index += 1
​
large = img.resize((10 * size, 10 * size))
large.show()
</pre>
