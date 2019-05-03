
# Code Page 936 (GBK) to UTF-8 Transcoder
# Author: Kristian Tang (@Krisiouz)
# A small script that converts a file encoded in Code Page 936 (GBK) to UTF-8.

def gbk_to_utf8(input_file, output_file):
    # Load Files
    print(input_file)
    print(output_file)

    input_file_opened = open(input_file, 'r', encoding='cp936')
    input_file_read = input_file_opened.read()
    output_file_opened = open(output_file, 'x', encoding='utf-8', newline='\n')
    # Transcode
    print('Transcode')
    output_file_opened.write(input_file_read)
    input_file_opened.close()
    output_file_opened.close()
    print('Done.\n')

def main():
    print('Code Page 936 (GBK) to UTF-8 Transcoder\n')
    gbk_to_utf8('sample.txt', 'sample.out')        
    # Ask the User Which File to Transcode
    #while 0 == 0:
    ##    input_file = input('Full file path of GBK file:\n')
    ##    print (input_file)
    #    output_file = input_file + '.utf-8'
    #    gbk_to_utf8(input_file, output_file)

if __name__ == '__main__':
    main()
