def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f if line.strip())


def compare_and_save(file1, file2):
    set1 = read_file(file1)
    set2 = read_file(file2)

    same = set1.intersection(set2)
    diff = set1.symmetric_difference(set2)

    with open('same.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(same)))

    with open('diff.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(diff)))


if __name__ == "__main__":
    # Створимо файли для тесту, якщо їх немає
    with open('file1.txt', 'w') as f: f.write("apple\nbanana\norange")
    with open('file2.txt', 'w') as f: f.write("banana\ngrape\napple")

    compare_and_save('file1.txt', 'file2.txt')
    print("Done! Check same.txt and diff.txt")