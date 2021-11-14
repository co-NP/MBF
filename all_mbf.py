import os

for i in range(2, 6):
	s = f"python3 gmbf.py {i} > MBF-{i}.csv"
	os.system(s)
