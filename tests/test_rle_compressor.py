import unittest
from compressors.rle_compressor import RLECompressor

class TestRLECompressor(unittest.TestCase):
    def setUp(self):
        self.compressor = RLECompressor()

    def test_compress(self):
        data = b'AABBBCCCC'
        compressed = self.compressor.compress(data)
        self.assertEqual(compressed, b'\x02A\x03B\x04C')

    def test_decompress(self):
        compressed = b'\x02A\x03B\x04C'
        decompressed = self.compressor.decompress(compressed)
        self.assertEqual(decompressed, b'AABBBCCCC')

    def test_compression_ratio(self):
        original_size = 100
        compressed_size = 75
        ratio = self.compressor.get_compression_ratio(original_size, compressed_size)
        self.assertEqual(ratio, 25.0)

if __name__ == '__main__':
    unittest.main()