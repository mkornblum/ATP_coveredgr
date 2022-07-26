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
        self.assertEqual(80, items[0].quality)

    def test_legendary_item_never_has_to_be_sold(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(1, items[0].sell_in)

    def test_legendary_item_quality_does_not_change_past_sell_by_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(80, items[0].quality)

    # TODO - convert next 3 tests to 1 parametrized test
    def test_sell_in_decreases_generic(self):
        items = [Item("generic item", 8, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(7, items[0].sell_in)

    def test_sell_in_decreases_brie(self):
        items = [Item("Aged Brie", 8, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(7, items[0].sell_in)

    def test_sell_in_decreases_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(7, items[0].sell_in)

    # TODO - convert next 3 tests to 1 parametrized test
    def test_sell_in_can_be_negative_generic(self):
        items = [Item("generic item", 0, 25)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_sell_in_can_be_negative_brie(self):
        items = [Item("Aged Brie", 0, 25)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_sell_in_can_be_negative_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_generic_item_quality_decreases_before_sell_by(self):
        items = [Item("generic item", 5, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(9, items[0].quality)

    def test_generic_item_quality_decreases_twice_as_fast_after_sell_by(self):
        items = [Item("generic item", 0, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(8, items[0].quality)

    def test_generic_item_quality_does_not_go_negative(self):
        items = [Item("generic item", 0, 0)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(0, items[0].quality)

    def test_brie_quality_increase_before_sell_by(self):
        items = [Item("Aged Brie", 5, 30)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(31, items[0].quality)

    def test_brie_quality_has_an_upper_limit(self):
        items = [Item("Aged Brie", 5, 50)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_pass_quality_has_an_upper_limit(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_brie_quality_increases_twice_as_fast_after_sell_by(self):
        items = [Item("Aged Brie", -1, 20)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(22, items[0].quality)






if __name__ == '__main__':
    unittest.main()
