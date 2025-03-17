str ="brontosaurus"

histogram = {}

for chr in str:
    histogram.setdefault(chr,0)
    histogram[chr] += 1

print(histogram)