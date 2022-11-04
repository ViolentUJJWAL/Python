import time
print("downloading");
for a in range(101):
	print(f"{a}%\r", end="")
	time.sleep(0.1)

print("DONE");