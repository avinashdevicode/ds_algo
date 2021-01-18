def reverse(lis: list) -> list:
    start_index = 0
    end_index = len(lis) - 1
    while start_index < end_index:
        lis[start_index], lis[end_index] = lis[end_index], lis[start_index]
        start_index += 1
        end_index -= 1


if __name__ == "__main__":
    n = [1,2,3, 4]
    reverse(n)
    print(n)
