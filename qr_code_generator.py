import qrcode # Imports the QR code library that handles all QR code generation logic.
from PIL import Image  #PIL (Python Imaging Library/Pillow) handles image creation and manipulation.

def generate_qr_code():
    """Generate a QR code from user input"""
    
    print("=" * 50)
    print("     QR CODE GENERATOR")
    print("=" * 50)
    print()
    
    # Get user input
    data = input("Enter the text or URL to encode: ")
    filename = input("Enter filename to save (without extension): ")
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size (minimum is 4)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(f"{filename}.png")
    
    print()
    print("=" * 50)
    print(f"✓ QR Code generated successfully!")
    print(f"✓ Saved as: {filename}.png")
    print("=" * 50)

def generate_colored_qr():
    """Generate a colored QR code"""
    
    print()
    print("=" * 50)
    print("     COLORED QR CODE GENERATOR")
    print("=" * 50)
    print()
    
    data = input("Enter the text or URL to encode: ")
    filename = input("Enter filename to save (without extension): ")
    
    print("\nColor options: red, blue, green, purple, orange")
    fill_color = input("Enter QR code color (or press Enter for black): ").lower()
    
    if not fill_color:
        fill_color = "black"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create colored image
    img = qr.make_image(fill_color=fill_color, back_color="white")
    img.save(f"{filename}.png")
    
    print()
    print("=" * 50)
    print(f"✓ Colored QR Code generated successfully!")
    print(f"✓ Color: {fill_color}")
    print(f"✓ Saved as: {filename}.png")
    print("=" * 50)

def main():
    """Main function to run the QR code generator"""
    
    print("\n" + "=" * 50)
    print("  WELCOME TO QR CODE GENERATOR")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Generate Standard QR Code")
        print("2. Generate Colored QR Code")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            generate_qr_code()
        elif choice == '2':
            generate_colored_qr()
        elif choice == '3':
            print("\nThank you for using QR Code Generator!")
            print("=" * 50)
            break
        else:
            print("\n⚠ Invalid choice! Please enter 1, 2, or 3.")
        
        print("\n")

if __name__ == "__main__":
    main()
