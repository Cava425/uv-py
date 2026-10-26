def permute(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(n)
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res


if __name__ == "__main__":
    import itertools

    for case in ([1, 2, 3], [0, 1], [1]):
        out = permute(case)
        assert sorted(out) == sorted(map(list, itertools.permutations(case)))
        print(case, "->", out)
