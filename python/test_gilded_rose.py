# -*- coding: utf-8 -*-
import unittest

from gilded_rose import* 


class GildedRoseTests(unittest.TestCase):
    
    def test_brie(self):
        """ Test the functionality of the AgedBrie subclass. """

        items = [AgedBrie("Aged Fine Wine", 5, 10)]
        gilded_rose = GildedRose(items)
        
        for i in range(8):
            print(i)
            gilded_rose.update_quality()

        # Check that sell_in decreases by 1
        self.assertEqual(-3, items[0].sell_in)
        # Check that quality increases by 1
        self.assertEqual(18, items[0].quality)
    
    
    def test_pass(self):
        """ Test the functionality of the BackstagePass subclass. """

        items = [BackstagePass("Backstage pass to a Biggie Shaz concert", 5, 10)]
        gilded_rose = GildedRose(items)
        
        for i in range(8):
            print(i)
            gilded_rose.update_quality()

        # Check that sell_in decreases by 1
        self.assertEqual(-3, items[0].sell_in)
        # Check that quality decreases to 0 after the sell date
        self.assertEqual(0, items[0].quality)

        items = [BackstagePass("Backstage pass to a Pirates Who Don't Do Anything concert", 10, 0)]
        gilded_rose = GildedRose(items)
        
        for i in range(8):
            print(i)
            gilded_rose.update_quality()

        # Check that sell_in decreases by 1
        self.assertEqual(2, items[0].sell_in)
        # Check that quality increases at an increasing rate
        self.assertEqual(20, items[0].quality)
    
    
    def test_sulfuras(self):
        """ Test the functionality of the Sulfuras subclass. """

        items = [Sulfuras("Sulfuras, Hand of Godrick the Grafted", 5, 80)]
        gilded_rose = GildedRose(items)
        
        for i in range(3):
            print(i)
            gilded_rose.update_quality()

        # Check that sell_in decreases by 1
        self.assertEqual(2, items[0].sell_in)
        # Check that quality doesn't change
        self.assertEqual(80, items[0].quality)
    
    
    def test_conjured(self):
        """ Test the functionality of the Conjured subclass. """

        items = [Conjured("Conjured Janzow eggs", 5, 10)]
        gilded_rose = GildedRose(items)
        
        for i in range(3):
            print(i)
            gilded_rose.update_quality()

        # Check that sell_in decreases by 1
        self.assertEqual(2, items[0].sell_in)
        # Check that quality decreases by 2
        self.assertEqual(4, items[0].quality)
    
    
    def test_normie(self):
        """ Test the funtionality of the NormieItem subclass. """
        
        items = [NormieItem("A disc golf disc", 5, 10)]
        gilded_rose = GildedRose(items)
        
        for i in range(3):
            print(i)
            gilded_rose.update_quality()

        # Check that sell_in decreases by 1
        self.assertEqual(2, items[0].sell_in)
        # Check that quality decreases by 1
        self.assertEqual(7, items[0].quality)
    
    

        
if __name__ == '__main__':
    unittest.main()
