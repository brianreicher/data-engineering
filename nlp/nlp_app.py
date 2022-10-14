from processor import Processor
import pprint as pp

def main():
    p = Processor()
    p1 = p.load_text('file1.txt', 'A')
    p2 = p.load_text('file2.txt', 'B')
    p3 = p.load_text('file3.txt', 'C')
    print(pp.pprint(p.data))


if __name__ == '__main__':
    main()
