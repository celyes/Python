def solution(digits):
    result = 0
    i = 0
    while i < len(digits)-4:
        if result < digits[i:i+5]:
            result = digits[i:i+5]
        i += 1
    return result
print solution('112239999556678999')