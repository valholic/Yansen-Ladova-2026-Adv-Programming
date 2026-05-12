import sys

def generate_pairs(genotype):
    pairs = []
    L = len(genotype)

    def backtrack(i, h1, h2):
        if i == L:
            pairs.append(("".join(h1), "".join(h2)))
            return

        if genotype[i] == '0':
            h1.append('0')
            h2.append('0')
            backtrack(i + 1, h1, h2)
            h1.pop()
            h2.pop()

        elif genotype[i] == '1':
            h1.append('1')
            h2.append('1')
            backtrack(i + 1, h1, h2)
            h1.pop()
            h2.pop()

        else:  # genotype[i] == '2'
            h1.append('0')
            h2.append('1')
            backtrack(i + 1, h1, h2)
            h1.pop()
            h2.pop()

            h1.append('1')
            h2.append('0')
            backtrack(i + 1, h1, h2)
            h1.pop()
            h2.pop()

    backtrack(0, [], [])
    return pairs


def solve_case(genotypes):
    all_haplotypes = set()

    possible_pairs = []

    for g in genotypes:
        pairs = generate_pairs(g)
        possible_pairs.append(pairs)

        for a, b in pairs:
            all_haplotypes.add(a)
            all_haplotypes.add(b)

    haplotypes = list(all_haplotypes)
    idx = {h: i for i, h in enumerate(haplotypes)}

    genotype_masks = []

    for pairs in possible_pairs:
        mask_options = []

        for a, b in pairs:
            mask = (1 << idx[a]) | (1 << idx[b])
            mask_options.append(mask)

        genotype_masks.append(mask_options)

    H = len(haplotypes)

    best = H

    def dfs(pos, used_mask):
        nonlocal best

        used_count = used_mask.bit_count()

        if used_count >= best:
            return

        if pos == len(genotypes):
            best = used_count
            return

        for pair_mask in genotype_masks[pos]:
            dfs(pos + 1, used_mask | pair_mask)

    dfs(0, 0)

    return best


def main():
    data = sys.stdin.read().strip().split()

    if not data:
        return

    idx = 0
    outputs = []

    while idx < len(data):
        N = int(data[idx])
        L = int(data[idx + 1])
        idx += 2

        genotypes = data[idx:idx + N]
        idx += N

        outputs.append(str(solve_case(genotypes)))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()