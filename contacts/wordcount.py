from WordCounter import WordCounter

def main():
    try:
        wc = WordCounter()
        wc.load('article.txt')
        wc.analysis()
        wc.print()
        wc.save('report.txt')
    except Exception as err:
        print('에러 : %s'%err)


if __name__ == '__main__':
    main()




