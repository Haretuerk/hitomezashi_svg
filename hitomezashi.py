import svgwrite
#from svgwrite import cm, mm   
from random import seed
from random import randint

# seed random number generator
seed(1)





dwg = svgwrite.Drawing('hitomezashi.svg', profile='tiny')

for line in range(40): 
    dashoffset = randint(0, 1)* 50
    dwg.add(dwg.line((0, 50*line), (3000, 50*line), stroke=svgwrite.rgb(0, 0, 0, '%'), stroke_width='1mm', stroke_dasharray='50,50',stroke_dashoffset=dashoffset))

for column in range(60): 
    dashoffset = randint(0, 1)* 50
    dwg.add(dwg.line((50*column,0), (50*column,2000), stroke=svgwrite.rgb(0, 0, 0, '%'), stroke_width='1mm', stroke_dasharray='50,50',stroke_dashoffset=dashoffset))


dwg.save()