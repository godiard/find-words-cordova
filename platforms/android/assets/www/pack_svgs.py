import os
import textwrap

images_path = './images/'


js_file = file('./js/svgbasket.js', 'w')

js_file.write('define(function (require) {\n')
js_file.write('\n')
js_file.write('svg = {};\n')
js_file.write('\n')

wrapper = textwrap.TextWrapper()
wrapper.width = 80

for filename in os.listdir(images_path):
    image_file_name = os.path.join(images_path, filename)
    if image_file_name.upper().endswith('SVG'):
        print 'SVG', image_file_name
        svg_content = file(image_file_name).read()
        svg_content = svg_content.replace("'", '"')
        lines = wrapper.wrap(svg_content)

        js_file.write("svg['%s'] = \n" % image_file_name)

        for line in lines:
            js_file.write("    '%s' +\n" % line)

        js_file.write("'';\n")
        js_file.write('\n')

js_file.write('return svg;\n')
js_file.write('\n')

js_file.write('});')

