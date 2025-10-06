words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]

palindromes = []
for w in words:
    if w == w[::-1]:
        palindromes.append(w)

print(palindromes)
