import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_split(path):
    ''' Split a pdf document into individual files, by passing the filename to be split. '''

    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))



def pdf_merge(path):
    ''' Merge multiple pdf's into a single file by passing the directory containing the files to be merged. '''

    pdf_writer = PdfFileWriter()

    for item in path:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    main()
