#import RLEString
import unittest
import sys

# Uncomment below for testing only, comment out before upload
 from rle import RLEString

class Assignment8Tests(unittest.TestCase):

	#--------------- test invalid strings ---------
	def test_invalid_string_numbers(self):
		string = "stringwithnumbers123"
		self.assertRaises(Exception, RLEString.RLEString, string)

	def test_invalid_string_special_chars(self):
		string = "specialChars_!"
		self.assertRaises(Exception, RLEString.RLEString, string)

	# -------------- test compress -----------------
	def test_already_compressed(self):
		rle = RLEString.RLEString("Hello")
		rle.compress()
		with self.assertRaises(Exception):
			rle.compress()

	def test_compressed_correctly(self):
		rle = RLEString.RLEString("Hello")
		hello_compressed = "1H1e2l1o"
		rle.compress()
		self.assertEqual(rle.__str__(), hello_compressed)

	# -------------- test decompress -----------------
	def test_already_decompressed(self):
		rle = RLEString.RLEString("Hello")
		#print(rle.compress())
		with self.assertRaises(Exception):
			rle.decompress()

	def test_decompressed_correctly(self):
		rle = RLEString.RLEString("Hello")
		hello_decompressed = "Hello"
		rle.compress()
		rle.decompress()
		self.assertEqual(rle.__str__(), hello_decompressed)

	# --------------- test iscompressed ---------------
	def test_iscompressed_true(self):
		rle = RLEString.RLEString("Hello")
		rle.compress()
		self.assertTrue(rle.iscompressed())


	def test_iscompressed_false(self):
		rle = RLEString.RLEString("Hello")
		self.assertFalse(rle.iscompressed())

	def test_iscompressed_after_decompress_false(self):
		rle = RLEString.RLEString("Hello")
		rle.compress()
		rle.decompress()
		self.assertFalse(rle.iscompressed())

	# -------------- test __str__ ---------------------
	def test_str(self):
		rle = RLEString.RLEString("Hello")
		self.assertEqual(rle.__str__(), "Hello")



if __name__ == '__main__':
    # Start the unit test
    unittest.main(verbosity=2)

