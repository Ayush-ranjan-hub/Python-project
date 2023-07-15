import qrcode
import os

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(filename)

def open_image(filename):
    os.system(f'open {filename}')  # Adjust for your operating system if needed

def generate_another():
    choice = input("Do you want to generate another QR code? (y/n): ")
    return choice.lower() == 'y'

def main():
    while True:
        print("Choose an option:")
        print("1. Generate QR code for a website")
        print("2. Generate QR code for a text")
        print("3. Exit")
        option = input("Enter your choice (1, 2, or 3): ")

        if option == '1':
            website = input("Enter the website URL: ")
            filename = "website_qr_code.png"
            generate_qr_code(website, filename)
            open_image(filename)
        elif option == '2':
            text = input("Enter the text: ")
            filename = "text_qr_code.png"
            generate_qr_code(text, filename)
            open_image(filename)
        elif option == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

        if not generate_another():
            print("Exiting the program...")
            break

if __name__ == "__main__":
    main()
