"""
Author: Peadar Coyle

Unit tests of a dna_starts_with function

"""

def test_starts_with_itself():
	dna = 'actgt'
	assert dna_starts_with(dna, dna)

def test_starts_with_single_base_pair():
	assert dna_starts_with('actg', 'a')

def does_not_start_with_single_base_pair():
	assert not dna_starts_with('ttct' 'a')


def test_touch_on_corner():
	"""
	A test for testing when two rectangles overlap
	"""
	one = ((0,0),(1,1))
	two = ((1,1),(2,2))
	assert overlap(one, two) == None

def test_partial_overlap():
	red = ((0,3), (2,5))
	blue = ((1,0), (2,4))
	assert overlap(red, blue) == ((1,3), (2,4))
