def intersection(x1,x2,w1,w2):
    start=max(x1,x2)
    end=min(x1+w1,x2+w2)
    if(end>start):
        return start,end-start
    return none,none


rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
x,w=intersection(rect1['left_x'],rect2['left_x'],rect1['width'],rect2['width'])
y,h=intersection(rect1['bottom_y'],rect2['bottom_y'],rect1['height'],rect2['height'])

print(x,y,w,h)