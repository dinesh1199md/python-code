input_Data="""
python 3.9 pypi
numpy 3 pypi
cherry 4
"""

out=[]

print(input_Data.strip().split('\n'))
for line in input_Data.strip().split('\n'):
    parts=line.split()
    # print(parts)
    if 'pypi' in parts:
        # print("in")
        out.append(f"{parts[0]}=={parts[1]}")

print("\n".join(out))