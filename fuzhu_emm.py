from svgpathtools import parse_path
d_string = ""
path_data = parse_path(d_string)
coords = [(segment.start.real, segment.start.imag) for segment in path_data]
print(coords)
def transform_coordinates(coordinates):
    transformed_coordinates = [{'x': coord[0], 'y': coord[1]} for coord in coordinates]
    return transformed_coordinates
z = transform_coordinates(coords)
z_str = repr(z).replace("},", "},\n")
print(z_str)





# function
# scaleCoordinates(drawing, b1, b2, k)
# {
#     let
# scaledDrawing = [];
# for (let i = 0; i < drawing.length; i++)
# {
#     let
# scaledX = (drawing[i].x + b1) * k;
# let
# scaledY = (drawing[i].y + b2) * k;
# scaledDrawing.push({'x': scaledX, 'y': scaledY});
# }
# return scaledDrawing;
# }
#
# let
# drawing_pre = [
# {'x': 0.0, 'y': 13.4},
# {'x': 8.09, 'y': 15.23},
# {'x': 14.870000000000001, 'y': 9.49},
# {'x': 20.61, 'y': 5.32},
# {'x': 30.26, 'y': 0.1},
# {'x': 35.260000000000005, 'y': 6.1},
# {'x': 38.650000000000006, 'y': 7.66},
# {'x': 44.13000000000001, 'y': 3.49},
# {'x': 49.57, 'y': 0.1},
# {'x': 57.13, 'y': 4.0},
# {'x': 61.300000000000004, 'y': 10.780000000000001},
# {'x': 57.91, 'y': 21.23},
# {'x': 48.589999999999996, 'y': 29.58},
# {'x': 26.87, 'y': 37.92},
# {'x': 2.61, 'y': 27.49}
# ];
# let
# drawing = scaleCoordinates(drawing_pre, 20, 30, 6)
#
# function
# setup()
# {
# createCanvas(600, 600);
# }
# function
# draw()
# {
# background(255);
# for (let i = 0; i < drawing.length; i++) {
#                                          // 用圆点表示每个坐标点
# point(drawing[i].x, drawing[i].y, 3);
# stroke('purple');
# strokeWeight(10);
# }
# }