import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height,width,cover):
    area = height * width 
    num_of_cans = math.ceil(area / cover)
    print(f"u will need {num_of_cans} number of cans")
paint_calc(height=test_h, width=test_w, cover=coverage)

