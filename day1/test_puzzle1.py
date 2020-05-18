#The unittest module is a python module for unit testing 
import unittest
import puzzle1

#This class is supposed to hold our unit tests which inherits from the imported unittest 
class TestBasic(unittest.TestCase):
    def test_pass(self):
        #This uses some of python's in built functions to read the file and divide it into lines
        data_file = open("input.txt", "r")
        data = puzzle1.parse(data_file.readlines())
        answer = puzzle1.solve(data)
        self.assertEqual(0, answer)

#Finds and runs all the tests if the file is run by calling python <filename> 
if __name__ == '__main__':
    unittest.main()