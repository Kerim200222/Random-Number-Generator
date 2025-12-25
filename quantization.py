from random_generator import LCG

rng = LCG()
quantization_table = [0] * 10

for _ in range(1000):
    value = rng.next_float()
    index = int(value * 10)
    quantization_table[index] += 1

print("Quantization Table:")
for i, count in enumerate(quantization_table):
    print(f"Range {i/10:.1f} - {(i+1)/10:.1f}: {count}")
