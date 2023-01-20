worlds = input().split()
palindrome = input()

result = [word for word in worlds if word == word[::-1]]
palindrome_count = result.count(palindrome)

print(result)
print(f"Found palindrome {palindrome_count} times")
