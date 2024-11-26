import sys
import subprocess
import datetime
import tempfile

from PIL import Image

def draw_image(img: Image, remote: str) -> None:
    with tempfile.TemporaryDirectory() as cwd:
        start_time = datetime.datetime.now() - datetime.timedelta(days=364) - datetime.timedelta((datetime.datetime.now().weekday() + 1) % 7)
        subprocess.run("git init", shell=True, cwd=cwd)
        for x in range(img.width):
            for y in range(img.height):
                time = start_time + datetime.timedelta(days=(7 * x) + y)
                for z in range(img.getpixel((x, y))):
                    subprocess.run(f"git -c commit.gpgsign=false commit --allow-empty --allow-empty-message -m '' --date='{time.isoformat()}'", shell=True, cwd=cwd)
        subprocess.run(f"git remote add origin {remote}", shell=True, cwd=cwd)
        subprocess.run("git push --set-upstream origin master", shell=True, cwd=cwd)


def process_image(image_path: str) -> Image:
    with Image.open(image_path) as img:
        # Resize the image to 52x7
        img = img.resize((52, 7))
        # Convert to grayscale
        img = img.convert("L")
        # Reduce to 5 levels of gray
        img = img.point(lambda x: x // 51 * 51)
        return img

def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python main.py <image_path> <git_repo_path>")
        return
    draw_image(process_image(sys.argv[1]), sys.argv[2])


if __name__ == "__main__":
    main()