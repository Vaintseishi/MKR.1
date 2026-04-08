def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f)


def process_files(file1, file2):
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    same = lines1.intersection(lines2)
    diff = lines1.symmetric_difference(lines2)

    with open('same.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(same)))

    with open('diff.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(diff)))