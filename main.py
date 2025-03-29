#COOL CONSOLE
import time
from PIL import Image

def pa(arr):
    [print(i) for i in arr]
def sa(arr):
    return sum(arr)/len(arr)
def cin(t=""):
    r = input(t)
    if r.is_digit():
        return int(r)
    if "." in r:
        g = r.split(".")[1]
        if g.is_digit():
            return float(r)
    return r
def convertImage(path):
    txt = []
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    grad = ' `.~i!g%#@'
    for x in range(0, im.height):
        str1 = ''
        for y in range(0, im.width):
            rgb = rgb_im.getpixel((y, x))
            sym = "#"
            rgb2 = [rgb[0], rgb[1], rgb[2]]
            if len(rgb) == 4 and rgb[3] <= 10:
                str1 += ' '
                continue
            str1 += grad[int((sa(rgb)-50)/25)]
        txt.append(str1)
    return txt
def check_box(text):
    print(f"\r |-|      {text} (y/n)", end="\r")
    g = input(" |")
    if g == "y":
        return True
    if g == "n":
        return False
def progress_bar(progress, total, length=50):
    coof = 100/length
    percent = length * (progress / float(total))
    per = percent*coof
    bar = "■"*int(percent) + "-" * (length - int(percent))
    #if int(percent) == 100:
    #    color = colorama.Fore.GREEN
    print(f"\r|{bar}| {per:.2f}%", end="\r")
def table(arr, t="r", name=""):
    g = [j for h in arr for j in h]
    #for j in arr:
    #    g.extend(j)
    max_g = max([len(str(h)) for h in g])
    if name:
        s = max_g*len(arr[0])
        f = s-len(name)
        f = f//2
        f += int((len(arr[0])-1)/2)
        print()
        print(f"{' '* f}{name}{' ' * f}")
        print()
    print("+"+"-"*(max_g*len(arr[0]))+"-"*(len(arr[0])-1)+"+")
    for n in arr:
        line = "|"
        for j in n:
            if t=="r":
                line += str(j)+" "*(max_g-len(str(j)))+"|"
            if t=="l":
                line += " "*(max_g-len(str(j)))+str(j)+"|"
            if t=="c":
                s = max_g
                f = s-len(str(j))
                f = f//2
                line += " "*f+str(j)+" "*f+"|"
        print(line)
        print("+"+"-"*(max_g*len(arr[0]))+"-"*(len(arr[0])-1)+"+")
def show_list(arr, ordered=True, name=""):
    if name: print(name+":")
    for x in range(len(arr)):
        start_sym = "●" if not ordered else str(x+1)
        print(f"    {start_sym}  {arr[x]}")
def resize_img(img, size):
    x, y = size
    if x < len(img[0]) and y < len(img):
        xc = int(len(img[0])/x)
        yc = int(len(img)/y)
        new_img = []
        for i in range(0, len(img), yc):
            s = ""
            for j in range(0, len(img[i]), xc):
                s += img[i][j]
            new_img.append(s)
        return new_img
def slash_anim(i):
    slash = eval('"////|||||\\\\\\\\\----"')
    index = i%len(slash)
    print(f"\r{slash[index]}", end="\r")



for x in range(100):
    progress_bar(x, 99)
    time.sleep(0.05)

    
print()


for x in range(100):
    print(f"\r        - {x+1} / 100", end="\r")
    slash_anim(x)
    time.sleep(0.05)
print()



arr1 = [
        ["A", "B", "C"],
        [12, 45, 1],
        [2344, 3232, 2],
        [4224, 3443, 3],
    ]
arr2 = ["Play games", "Watch videos", "Eat crips"]
img = convertImage("ClipWindowsGIF.gif")
#print(len(img[0]), len(img))


print()


table(arr1, name="Table1")
show_list(arr2, name="To do", ordered=False)
print(check_box("Hello world"))
pa(resize_img(img, [25, 25]))
input()

