import unittest
#import pronto


class TestPronto(unittest.TestCase):

    # Ensures PiCamera starts up
    def test_camera_setup(self):
        #self.assertTrue(pronto.camera)
        return

    # Ensures camera takes picture (take_pic)
    def test_take_pic(self):
        pass

    # Ensures image is opened properly (send_pic)
    def test_open_pic(self):
        #self.assertIsNotNone(pronto.send_pic.image)
        return

    # Ensures image is uploaded properly (send_pic)
    def test_send_pic(self):
        #self.assertIsNotNone(
        pass

# Runs unit test
if __name__ == '__main__':
    unittest.main()