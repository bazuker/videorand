def serialize_pixel(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    return r*g*b*(r+g+b)


def serialize_chunk(chunk):
    height = len(chunk)-1
    if height < 1:
        return 1

    width = len(chunk[0])-1
    if width < 1:
        return 1

    sum = 0
    for x in range(0, width):
        for y in range(0, height):
            sum += serialize_pixel(chunk[x, y])
    return sum


def serialize_frame(frame, width, height, chunk_size):
    x = 0
    y = 0
    sum = 0
    while True:
        sum += serialize_chunk(frame[x:x + chunk_size, y:y + chunk_size])
        x += chunk_size
        if x >= width:
            x = 0
            y += chunk_size
            if y >= height:
                break
    return sum
