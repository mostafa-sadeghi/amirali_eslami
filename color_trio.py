import unittest


def color_trio(colors):
    new_colors = list(colors)
    while len(new_colors) > 1:
        output = []
        for i in range(len(new_colors)-1):

            if new_colors[i] == new_colors[i+1]:
                output += new_colors[i]
            else:
                temp = list('ryb')

                output += 'ryb'.replace(new_colors[i],
                                        '').replace(new_colors[i+1], '')
        else:
            new_colors = output
    return ''.join(new_colors)


class TestColor(unittest.TestCase):
    def test_color(self):
        self.assertEqual(color_trio('y'), 'y')
        self.assertEqual(color_trio('bb'), 'b')
        self.assertEqual(color_trio('rybyry'), 'r')
        self.assertEqual(color_trio('brybbr'), 'r')
        self.assertEqual(color_trio('rbyryrrbyrbb'), 'y')
        self.assertEqual(color_trio('yrbbbbryyrybb'), 'b')


unittest.main()
# def colour_trio(colours):
#     # runs until colours contains only one singleton element
#     while len(colours) > 1:
#         # empty string to store the final colours of a row
#         row = ""
#         # iterating over colours by indexing
#         for i in range(len(colours)-1):
#             # extracting two consecutive colours
#             c1, c2 = colours[i], colours[i+1]
#         # if both colours are same
#             if c1 == c2:
#                 row += c1
#             else:
#                 # replacing c1 and c2 with emtpy space, result remaining colour
#                 # and appending resulting colour to row
#                 row += "ybr".replace(c1, "").replace(c2, "")
#         else:
#             # updating colours with row
#             colours = row
#     # returns final row, colours
#     return colours
