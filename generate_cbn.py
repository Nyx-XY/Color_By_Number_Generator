from typing import Union
from PIL import Image
import io
import argparse
import ast

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transform an images into 'color by numbers' pictures."
    )
    parser.add_argument(
        "images",
        type=str,
        nargs="*",
        help="The images to convert. Can include multiple. These can be locations of image file paths or byte strings representing the data in these files. If using anything other than paths this should be reflected in the format flag.",
        metavar="[IMG1 IMG2 IMG3 ...]",
    )
    parser.add_argument(
        "--test",
        "-t",
        action="store_true",
        help="Run test mode. Will ignore most other flags.",
        dest="test",
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        default="path",
        help='Format to interpret images as. One of: "path", "bytes"',
        metavar="fmt",
        dest="fmt",
    )
    parser.add_argument(
        "--paths",
        type=str,
        nargs="+",
        default=[],
        help="List of image file paths.",
        dest="paths",
    )
    parser.add_argument(
        "--bytes",
        type=str,
        nargs="+",
        default=[],
        help="List of image byte strings.",
        dest="bytes",
    )

    args = parser.parse_args()


def generate(img: Union[Image.Image, str, bytes]) -> Image:
    if isinstance(img, bytes):
        return generate(Image.open(io.BytesIO(img)))
    elif isinstance(img, str):
        return generate(Image.open(img))
    elif not isinstance(img, Image.Image):
        raise TypeError(f"Don't know what to do with argument {img} ({type(img)})")


if __name__ == "__main__":
    if args.test:
        s = ast.literal_eval(f"b'{args.images[0]}'")
        img = Image.open(io.BytesIO(s))
        img.show()
        # img_byte_arr = io.BytesIO()
        # Image.open("imgs/4cols-16.jpg").save(img_byte_arr, format="PNG")
        # img_byte_arr = img_byte_arr.getvalue()
        # print(img_byte_arr)
    else:
        for img in args.images:
            if args.fmt == "bytes":
                img = ast.literal_eval(f"b'{img}'")
            generate(img)
