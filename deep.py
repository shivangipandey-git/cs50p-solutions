answer= input("What's the answer to the Great Question of Life, the Universe and Everything?")
life= answer.strip().lower()
if (life== "42" or life=="forty-two" or life== "forty two"):
    print("Yes")
else:
    print("No")
