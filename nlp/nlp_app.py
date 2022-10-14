import pprint as pp
from processor import Processor
import parsers

def main():
    p = Processor()
    p.load_text('file1.txt', 'A')
    p.load_text('file2.txt', 'B')
    p.load_text('file3.txt', 'C')
    p.load_text(file_name='authors.json', label='J', parser=parsers.Parser.json_parser)
    print(pp.pprint(p.data))
    p.compare_num_words()


if __name__ == '__main__':
    main()
