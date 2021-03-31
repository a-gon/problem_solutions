def parse_string(text):
    output = []
    lines = text.splitlines()
    lines.pop(0)

    for line in lines:
        out = line.split('|')
        output.append([out[0].strip(), out[3].strip()])

    return output

text = """Server	Col1	Col2	Status	Avail
Server A    |   n12j3Hfe-sfs |   u12j3Hfe  |   -up  |   yes
Sever B     |   n22h3Hfe |   nsjd5q0bu  |   -down   |   no"""


output = parse_string(text)
for i in output:
    print(f'{i[0]} : {i[1]}')


