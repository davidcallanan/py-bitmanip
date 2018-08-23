# In this module, 0 is considered the least significant bit

def bitmask(start=0, end=None):
	if end == None or end == start:
		return 0b1 << start
	mask = 1
	for _ in range(0, end - start):
		mask = mask << 1
		mask += 1
	return mask << start

def getbits(x, mask):
	y = x & mask
	while mask & 0b1 == 0b0:
		mask = mask >> 1
		y = y >> 1
	return y

def setbits(x, mask, y):
	mask2 = mask
	while mask2 & 0b1 == 0b0:
		mask2 = mask2 >> 1
	z = getbits(y, mask2)
	x &= ~mask
	while mask & 0b1 == 0b0:
		mask = mask >> 1
		z = z << 1
	return x + z