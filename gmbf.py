import sys

def CheckUnion(X, Y):
	l = len(X)
	for i in range(l):
		if int(X[i]) | int(Y[i]) != int(Y[i]):
			return False
	return True


def MBF(n):
	if n == 0:
		return ["0", "1"]
	else:
		mbf = []
		F  = MBF(n - 1)
		for f in F:
			for g in F:
				if CheckUnion(f, g):
					mbf.append(f + g)
		return mbf


def GenerateMBF(n):
	A = MBF(n)
	s = ""
	for i in range(2 ** n):
		s += f"f{i + 1},"
	s += "d\n"
	s += "c, " * (2 ** n + 1)
	s = s[:-2]

	print(s)
	for i in range(len(A)):
		s = ""
		for j in range(len(A[0])):
			s += f"{A[i][j]}, "
		s += f"{i + 1}"
		print(s)

# main
if len(sys.argv) == 2:
	n = int(sys.argv[1])
	GenerateMBF(n)
else:
	print("gmbf <n>")


