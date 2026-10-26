if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    k = 2

    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    print(counts)

    print(counts.items())

    top_k = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]

    print([num for num, count in top_k])

