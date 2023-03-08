require File.join(File.dirname(__FILE__), "gilded_rose")

describe GildedRose do
  describe "#update_quality" do
    it "legendary item quality does not decrease" do
      items = [Item.new("Sulfuras, Hand of Ragnaros", 20, 80)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(80)
    end

    it "legendary item never has to be sold" do
      items = [Item.new("Sulfuras, Hand of Ragnaros", 1, 80)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(1)
    end

    it "legendary item quality does not change past sell by date" do
      items = [Item.new("Sulfuras, Hand of Ragnaros", -1, 80)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(80)
    end

    # TODO - convert next 3 tests to 1 parametrized test
    it "generic item sell_in decreases" do
      items = [Item.new("generic item", 8, 10)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(7)
    end

    it "test_sell_in_decreases_brie" do
      items = [Item.new("Aged Brie", 8, 10)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(7)
    end

    it "test_sell_in_decreases_backstage_pass" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 8, 10)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(7)
    end

    # TODO - convert next 3 tests to 1 parametrized test
    it "test_sell_in_can_be_negative_generic_item" do
      items = [Item.new("generic item", 0, 25)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(-1)
    end

    it "test_sell_in_can_be_negative_brie" do
      items = [Item.new("Aged Brie", 0, 25)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(-1)
    end

    it "test_sell_in_can_be_negative_backstage_pass" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 0, 25)]
      GildedRose.new(items).update_quality
      expect(items[0].sell_in).to eq(-1)
    end

    it "test_generic_item_quality_decreases_before_sell_by" do
      items = [Item.new("generic item", 5, 10)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(9)
    end

    it "test_generic_item_quality_decreases_twice_as_fast_after_sell_by" do
      items = [Item.new("generic item", 0, 10)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(8)
    end

    it "test_generic_item_quality_does_not_go_negative" do
      items = [Item.new("generic item", 0, 0)]
      GildedRose.new(items).update_quality
      expect(0).to eq(items[0].quality)
    end

    it "test_brie_quality_increase_before_sell_by" do
      items = [Item.new("Aged Brie", 5, 30)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(31)
    end

    it "test_brie_quality_has_an_upper_limit" do
      items = [Item.new("Aged Brie", 5, 50)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(50)
    end

    it "test_backstage_pass_quality_has_an_upper_limit" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 15, 50)]
      GildedRose.new(items).update_quality
      expect(items[0].quality).to eq(50)
    end

    it "test_brie_quality_increases_twice_as_fast_after_sell_by" do
      items = [Item.new("Aged Brie", -1, 20)]
      GildedRose.new(items).update_quality
      expect(22).to eq(items[0].quality)
    end

    it "test_brie_quality_has_upper_limit_even_when_really_old" do
      items = [Item.new("Aged Brie", -99, 50)]
      GildedRose.new(items).update_quality
      expect(50).to eq(items[0].quality)
    end

    it "test_backstage_pass_quality_increases_each_day_when_concert_date_is_far_off_in_future" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 30, 23)]
      GildedRose.new(items).update_quality
      expect(24).to eq(items[0].quality)
    end

    it "test_backstage_pass_quality_increases_more_as_concert_date_gets_closer" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
      GildedRose.new(items).update_quality
      expect(42).to eq(items[0].quality)
    end

    it "test_backstage_pass_quality_increases_much_more_when_concert_date_is_close" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 5, 40)]
      GildedRose.new(items).update_quality
      expect(43).to eq(items[0].quality)
    end

    it "test_backstage_pass_quality_drops_to_zero_when_concert_has_passed" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
      GildedRose.new(items).update_quality
      expect(0).to eq(items[0].quality)
    end

    it "test_backstage_pass_quality_respects_maximum_value_even_when_concert_is_near" do
      items = [Item.new("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
      GildedRose.new(items).update_quality
      expect(50).to eq(items[0].quality)
    end

    it "test_shop_contains_multiple_items_and_all_are_updated" do
      items = [Item.new("Sulfuras, Hand of Ragnaros", 0, 80),
        Item.new("generic item", 10, 5)]
      GildedRose.new(items).update_quality

      expect(items[0].sell_in).to eq(0)
      expect(items[1].sell_in).to eq(9)
    end
  end
end
