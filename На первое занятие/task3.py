def negative_pixel (pixel):
    negative = 255 - pixel
    return negative

def main ():
    pixel = int(input("Введите изначальное целочисленное значение цвета пикселя: "))
    pixel_ready = negative_pixel(pixel)
    print (f"Цвет пикселя в негативе: {pixel_ready}")

main()