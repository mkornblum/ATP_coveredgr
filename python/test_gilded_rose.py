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
    def test_sell_in_decreases_generic_item(self):
        items = [Item("generic item", 8, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(7, items[0].sell_in)

    def test_sell_in_decreases_brie(self):
        items = [Item("Aged Brie", 8, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(7, items[0].sell_in)

    def test_sell_in_decreases_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 10)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(7, items[0].sell_in)

    # TODO - convert next 3 tests to 1 parametrized test
    def test_sell_in_can_be_negative_generic_item(self):
        items = [Item("generic item", 0, 25)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_sell_in_can_be_negative_brie(self):
        items = [Item("Aged Brie", 0, 25)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_sell_in_can_be_negative_backstage_pass(self):
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

    def test_backstage_pass_quality_has_an_upper_limit(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 50)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_brie_quality_increases_twice_as_fast_after_sell_by(self):
        items = [Item("Aged Brie", -1, 20)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(22, items[0].quality)

    def test_brie_quality_has_upper_limit_even_when_really_old(self):
        items = [Item("Aged Brie", -99, 50)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_backstage_pass_quality_increases_each_day_when_concert_date_is_far_off_in_future(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 30, 23)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(24, items[0].quality)

    def test_backstage_pass_quality_increases_more_as_concert_date_gets_closer(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(42, items[0].quality)

    def test_backstage_pass_quality_increases_much_more_when_concert_date_is_close(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 40)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(43, items[0].quality)

    def test_backstage_pass_quality_drops_to_zero_when_concert_has_passed(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_quality_respects_maximum_value_even_when_concert_is_near(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_shop_contains_multiple_items_and_all_are_updated(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80),
                 Item("generic item", 10, 5)]
        sut = GildedRose(items)

        sut.update_quality()

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(9, items[1].sell_in)

if __name__ == '__main__':
    unittest.main()
