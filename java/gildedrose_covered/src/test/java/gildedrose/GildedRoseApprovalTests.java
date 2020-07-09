package gildedrose;

import org.approvaltests.Approvals;
import org.approvaltests.combinations.CombinationApprovals;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GildedRoseApprovalTests {

    @Test
    public void test_UpdateQuality_SingleItem_AtSellin_NoQuality() {
        Item[] items = new Item[]{new Item("normal", 0, 0)};
        GildedRose sut = new GildedRose(items);
        sut.updateQuality();
        assertEquals("normal, -1, 0", sut.items[0].toString());
        Approvals.verify(sut.items[0].toString());
    }

    @Test
    public void test_UpdateQuality_SingleItem() {
        CombinationApprovals.verifyAllCombinations(
                this::doUpdateQuality,
                new String[] {"foo", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"},
                new Integer[] {-1, 0, 5, 10, 11},    // SellIn
                new Integer[] { 0, 1, 49, 50 }       // Quality
        );
    }

    private String doUpdateQuality(String name, int sellIn, int quality) {
        Item[] items = new Item[]{new Item(name, sellIn, quality)};
        GildedRose sut = new GildedRose(items);
        sut.updateQuality();
        return sut.items[0].toString();
    }
}
