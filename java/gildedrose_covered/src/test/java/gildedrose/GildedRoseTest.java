package gildedrose;

import gildedrose.Item;
import gildedrose.GildedRose;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GildedRoseTest {

    public static final String BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert";

    private Item[] createItemArray(String itemName, int sellIn, int quality) {
        return new Item[] { new Item(itemName, sellIn, quality) };
    }

    @Test
    public void LegendaryItem_QualityDoesNotDecrease() {
        // Arrange
        GildedRose app = new GildedRose(createItemArray("Sulfuras, Hand of Ragnaros", 20, 80));

        // Act
        app.updateQuality();

        // Assert
        assertEquals(80, app.items[0].quality, "Quality is not decreased for this legendary item");
    }

    @Test
    public void LegendaryItem_NeverHasToBeSold() {
        GildedRose app = new GildedRose(createItemArray("Sulfuras, Hand of Ragnaros", 1, 80));
        app.updateQuality();
        assertEquals(1, app.items[0].sellIn, "Sellin is not decreased for this legendary item");
    }

    @Test
    public void GenericItem_SellinDecreasesEachUpdate() {
        GildedRose app = new GildedRose(createItemArray("generic item", 8, 10));
        app.updateQuality();
        assertEquals(7, app.items[0].sellIn, "Item sellin date should decrease by 1 each day");
    }

    @Test
    public void GenericItem_SellinDateGoesNegative() {
        GildedRose app = new GildedRose(createItemArray("generic item", 0, 25));
        app.updateQuality();
        assertEquals(-1, app.items[0].sellIn, "Sellin date will go negative once sellin date is reached");
    }

    @Test
    public void GenericItem_QualityDecreasesBeforeSellinDate() {
        GildedRose app = new GildedRose(createItemArray("generic item", 5, 10));
        app.updateQuality();
        assertEquals(9, app.items[0].quality, "Item quality should only decrease by 1 each day");
    }

    @Test
    public void GenericItem_QualityDecreasesTwiceAsFastAfterSellinDate() {
        GildedRose app = new GildedRose(createItemArray("generic item", 0, 10));
        app.updateQuality();
        assertEquals(8, app.items[0].quality, "When sellin date is 0 then quality decreases twice as fast");
    }

    @Test
    public void GenericItem_QualityNeverGoesNegative() {
        GildedRose app = new GildedRose(createItemArray("generic item", 0, 0));
        app.updateQuality();
        assertEquals(0, app.items[0].quality, "Quality will not go negative once it is zero");
    }

    @Test
    public void AgedBrie_QualityIncreases() {
        GildedRose app = new GildedRose(createItemArray("Aged Brie", 5, 30));
        app.updateQuality();
        assertEquals(31, app.items[0].quality, "Aged Brie increases quality with age");
    }

    @Test
    public void AgedBrie_QualityIsCappedAt50() {
        GildedRose app = new GildedRose(createItemArray("Aged Brie", 5, 50));
        app.updateQuality();
        assertEquals(50, app.items[0].quality, "Quality has an upper limit that is not exceeded");
    }

    @Test
    public void AgedBrie_QualityIncreases_EvenAfterSellInDate() {
        GildedRose app = new GildedRose(createItemArray("Aged Brie", -1, 20));
        app.updateQuality();
        assertEquals(22, app.items[0].quality, "Aged Brie improves twice as fast after sellin date (BUG?)");
    }

    @Test
    public void AgedBrie_QualityIsCappedAt50_EvenWhenReallyOld() {
        GildedRose app = new GildedRose(createItemArray("Aged Brie", -99, 50));
        app.updateQuality();
        assertEquals(50, app.items[0].quality, "Quality has an upper limit, even when cheese is old");
    }

    @Test
    public void BackstagePass_QualityIncreasesEachDay() {
        GildedRose app = new GildedRose(createItemArray(BACKSTAGE_PASS, 30, 23));
        app.updateQuality();
        assertEquals(24, app.items[0].quality, "Backstage Pass increases quality with age");
    }

    @Test
    public void BackstagePass_QualityIncreasesMoreAsConcertNears() {
        GildedRose app = new GildedRose(createItemArray(BACKSTAGE_PASS, 10, 40));
        app.updateQuality();
        assertEquals(42, app.items[0].quality, "Backstage Pass quality increases more when concert is near");
    }

    @Test
    public void BackstagePass_QualityIncreasesMuchMoreWhenConcertIsClose() {
        GildedRose app = new GildedRose(createItemArray(BACKSTAGE_PASS, 5, 40));
        app.updateQuality();
        assertEquals(43, app.items[0].quality, "Backstage Pass quality increases even more when concert is almost here");
    }

    @Test
    public void BackstagePass_QualityIsCappedAt50() {
        GildedRose app = new GildedRose(createItemArray(BACKSTAGE_PASS, 40, 50));
        app.updateQuality();
        assertEquals(50, app.items[0].quality, "Quality has an upper limit that is not exceeded");
    }

    @Test
    public void BackStagePass_QualityDropsToZeroWhenConcertPasses() {
        GildedRose app = new GildedRose(createItemArray(BACKSTAGE_PASS, 0, 50));
        app.updateQuality();
        assertEquals(0, app.items[0].quality, "Backstage Pass is worthless when concert has passed");
    }

    //TODO: NEW BEHAVIOR
    // conjured items
}
