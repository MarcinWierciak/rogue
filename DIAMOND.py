def diamond(n):
    if n%2 == 0 or n < 0:
        return None

    result = []
    middle = n//2 + 1
    print(middle)

    for i in range(0,middle):
        star_count = n - i * 2
        length = star_count + i
        line = ("*" * star_count).rjust(length)
        result.append(line)
        if i > 0 :
            result.insert(0, line)

    return "\n".join(result) + "\n"

if __name__ == "__main__":
    print(diamond(5))
    print(diamond(7))
    print(diamond(13))
