import argparse
import io
from PIL import Image

parser = argparse.ArgumentParser(description="Get the byte string of an image.")
parser.add_argument(
    "img", type=str, nargs=1, help="An image file location", metavar="IMG"
)
parser.add_argument(
    "--format",
    "-f",
    type=str,
    default=None,
    help="Format to save image as. Default copies input MIME.",
    metavar="fmt",
    dest="fmt",
)
args = parser.parse_args()

if __name__ == "__main__":
    b = io.BytesIO()
    if args.fmt is None:
        mime = args.img[0].split(".")[-1]
        args.fmt = {"jpg": "jpeg"}.get(mime, mime)
    Image.open(args.img[0]).save(b, format=args.fmt)
    print(str(b.getvalue())[2:-1])
