import qrcode
import typer

app = typer.Typer()


def generate_qr_code(data: str, output_file: str) -> None:
    """
    Generates a QR code from the input data and saves it to a PNG file.

    Parameters:
    - data (str): The data to encode in the QR code.
    - output_file (str): The filename to save the QR code as PNG.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)
    print(f"QR code saved to {output_file}")


@app.command()
def create(data: str, output: str) -> None:
    """
    Create a QR code and save it as a PNG file.

    Arguments:
    - data: The data to encode in the QR code.
    - output: The output PNG file name.
    """
    generate_qr_code(data, output)


if __name__ == "__main__":
    app()
