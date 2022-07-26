# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_legendary_item_quality_does_not_decrease(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]
        sut = GildedRose(items)

        # Act
        sut.update_quality()

        # Assert
        self.assertEquals(80, items[0].quality)

    def test_legendary_item_never_has_to_be_sold(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEquals(1, items[0].sell_in)




if __name__ == '__main__':
    unittest.main()