from reportlab.lib.pagesizes import a4
from reportlab.pdfgen import canvas
from reportlab.lin import colors

def create_pdf(data_row, output_pdf, image_path):
    # Create the file
    file_canvas = canvas.Canvas(output_pdf, pagesize=a4)
    width, height = a4

    # Image
    # TODO

    # Add informations
    # TODO

    # Save
    file_canvas.save()

def main():
    print("This is my prog")

if __name__ == "__main__" :
    main()
