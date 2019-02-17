import math
def compass(dx,dy,sx,sy):
    del_x=dx-sx
    del_y=dy-sy
    angle=math.atan2(del_x,del_y)/math.pi*180
    if angle<0:
        fangle=360+angle
    else:
        fangle=angle
    comp=['Here','NE','E','SE','S','SW','W','NW','N']
    compass_look=round(fangle/45)
    return comp[compass_look],fangle
print(compass(1,1,4,4))
