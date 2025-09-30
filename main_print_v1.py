# 변수 정의
name = "kimminwoo"
age = 23
score = 96.5

# 1. 기본 출력
print("Hello, Python!")

# 2. 여러 값 출력 (콤마 구분 → 자동 띄어쓰기)
print("Name:", name, "Age:", age, "Score:", score)

# 3. f-string (Python 3.6 이상)
print(f"My name is {name}, I am {age} years old, score: {score}")

# 4. format() 함수
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
print("My name is {0}, Age: {1}, Score {2}".format(name, age, score))
print("Score with 2 decimals: {:.2f}".format(score))

# 5. % 포맷팅 (C 스타일)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# 6. 여러 줄 출력 (\n)
print("This is line 1\nThis is line 2")

# 7. end 옵션
print("Hello", end=" ")
print("World!")

# 8. sep 옵션
print("2025", "09", "23", sep="-")

# 9. 딕셔너리 같이 출력
data = {"name": name, "age": age, "score": score}
print("Data:", data)

# 10. f-string 계산/함수
print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

# 11. 멀티라인 f-string
info = f"""
- Name : {name}
- Age  : {age}
- Score: {score:.2f}
"""
print(info)
