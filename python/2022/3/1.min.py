print(sum([[ord(s)-ord('A')+27 if ord(s)<ord('a') else ord(s)-ord('a')+1 for s in x[:len(x)//2] if s in x[len(x)//2:]][0] for x in open('i').readlines()]))
