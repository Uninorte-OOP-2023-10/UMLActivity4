import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath(os.pardir)))
sys.path.insert(2, os.path.join(os.path.abspath(os.pardir), 'src'))

import unittest

if __name__ == '__main__':
    unittest.main()