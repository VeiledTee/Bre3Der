import pandas as pd
import treelib

CSV_FILE = "phylogenetic.csv"
# LINE_TYPE = "ascii-ex"  # single lines
LINE_TYPE = "ascii-exr"  # single lines and curved subtree indicator
# LINE_TYPE = "ascii-em"  # double lines horizontally and vertically
# LINE_TYPE = "ascii-emh"  # double lines horizontally
# LINE_TYPE = "ascii-emv"  # double lines vertically


tree = pd.read_csv(CSV_FILE)
parent_child = tree[['Parent', 'Child']]

# determine all children of cube or pyramid
cube = []
pyramid = []

for row in parent_child.itertuples():
	if row[1].lower() == 'cube' or row[1].lower() in cube:
		cube.append(row[2].lower())
	elif row[1].lower() == 'pyramid' or row[1].lower() in pyramid:
		pyramid.append(row[2].lower())

# generate trees
cube_tree = treelib.Tree()
cube_tree.create_node('Cube', 'cube')

pyramid_tree = treelib.Tree()
pyramid_tree.create_node("Pyramid", "pyramid")

for index, row in parent_child.iterrows():
	parent = row['Parent'].lower()
	child = row['Child'].lower()
	if parent == 'cube' or parent in cube:
		cube_tree.create_node(identifier=child, parent=parent)
	elif parent == 'pyramid' or parent in pyramid:
		pyramid_tree.create_node(identifier=child, parent=parent)
	else:
		print("You goofed")

if __name__ == "__main__":
	# save trees
	cube_tree.save2file(filename="cube_tree.txt", line_type=LINE_TYPE)
	pyramid_tree.save2file(filename="pyramid_tree.txt", line_type=LINE_TYPE)
