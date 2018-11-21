using NUnit.Framework;
using System.Collections.Generic;

namespace csharp
{
    [TestFixture]
    public class GildedRoseTest
    {
        private const string BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert";

        private List<Item> createItemList(string itemName, int sellIn, int quality) {
            return new List<Item> { new Item { Name = itemName, SellIn = sellIn, Quality = quality } };
        }        

        [Test]
        public void LegendaryItem_QualityDoesNotDecrease() {
            // Arrange
            GildedRose sut = new GildedRose(createItemList("Sulfuras, Hand of Ragnaros", 20, 80));
    
            // Act
            sut.UpdateQuality();
    
            // Assert
            Assert.AreEqual(80, sut.Items[0].Quality, "Quality is not decreased for this legendary item");
        }
    
        [Test]
        public void LegendaryItem_NeverHasToBeSold() {
            GildedRose sut = new GildedRose(createItemList("Sulfuras, Hand of Ragnaros", 1, 80));
            sut.UpdateQuality();
            Assert.AreEqual(1, sut.Items[0].SellIn, "Sellin is not decreased for this legendary item");
        }

        [TestCase("generic item")]
        [TestCase("Aged Brie")]
        [TestCase(BACKSTAGE_PASS)]
        public void NonLegendaryItem_SellInDate_Decreases(string name) {
            GildedRose sut = new GildedRose(createItemList(name, 8, 10));
            sut.UpdateQuality();
            Assert.AreEqual(7, sut.Items[0].SellIn, "Item sellin date should decrease by 1 each day");
        }
    
        [Test]
        public void GenericItem_SellinDateGoesNegative() {
            GildedRose sut = new GildedRose(createItemList("generic item", 0, 25));
            sut.UpdateQuality();
            Assert.AreEqual(-1, sut.Items[0].SellIn, "Sellin date will go negative once sellin date is reached");
        }
    
        [Test]
        public void GenericItem_QualityDecreasesBeforeSellinDate() {
            GildedRose sut = new GildedRose(createItemList("generic item", 5, 10));
            sut.UpdateQuality();
            Assert.AreEqual(9, sut.Items[0].Quality, "Item quality should only decrease by 1 each day");
        }
    
        [Test]
        public void GenericItem_QualityDecreasesTwiceAsFastAfterSellinDate() {
            GildedRose sut = new GildedRose(createItemList("generic item", 0, 10));
            sut.UpdateQuality();
            Assert.AreEqual(8, sut.Items[0].Quality, "When sellin date is 0 then quality decreases twice as fast");
        }
    
        [Test]
        public void GenericItem_QualityNeverGoesNegative() {
            GildedRose sut = new GildedRose(createItemList("generic item", 0, 0));
            sut.UpdateQuality();
            Assert.AreEqual(0, sut.Items[0].Quality, "Quality will not go negative once it is zero");
        }
    
        [Test]
        public void AgedBrie_QualityIncreases() {
            GildedRose sut = new GildedRose(createItemList("Aged Brie", 5, 30));
            sut.UpdateQuality();
            Assert.AreEqual(31, sut.Items[0].Quality, "Aged Brie increases quality with age");
        }
    
        [Test]
        public void AgedBrie_QualityIsCappedAt50() {
            GildedRose sut = new GildedRose(createItemList("Aged Brie", 5, 50));
            sut.UpdateQuality();
            Assert.AreEqual(50, sut.Items[0].Quality, "Quality has an upper limit that is not exceeded");
        }
    
        [Test]
        public void AgedBrie_QualityIncreases_EvenAfterSellInDate() {
            GildedRose sut = new GildedRose(createItemList("Aged Brie", -1, 20));
            sut.UpdateQuality();
            Assert.AreEqual(22, sut.Items[0].Quality, "Aged Brie improves twice as fast after sellin date (BUG?)");
        }
    
        
        [Test]
        public void AgedBrie_QualityIsCappedAt50_EvenWhenReallyOld() {
            GildedRose sut = new GildedRose(createItemList("Aged Brie", -99, 50));
            sut.UpdateQuality();
            Assert.AreEqual(50, sut.Items[0].Quality, "Quality has an upper limit, even when cheese is old");
        }
    
        [Test]
        public void BackstagePass_QualityIncreasesEachDay() {
            GildedRose sut = new GildedRose(createItemList(BACKSTAGE_PASS, 30, 23));
            sut.UpdateQuality();
            Assert.AreEqual(24, sut.Items[0].Quality, "Backstage Pass increases quality with age");
        }
    
        [Test]
        public void BackstagePass_QualityIncreasesMoreAsConcertNears() {
            GildedRose sut = new GildedRose(createItemList(BACKSTAGE_PASS, 10, 40));
            sut.UpdateQuality();
            Assert.AreEqual(42, sut.Items[0].Quality, "Backstage Pass quality increases more when concert is near");
        }
    
        [Test]
        public void BackstagePass_QualityIncreasesMuchMoreWhenConcertIsClose() {
            GildedRose sut = new GildedRose(createItemList(BACKSTAGE_PASS, 5, 40));
            sut.UpdateQuality();
            Assert.AreEqual(43, sut.Items[0].Quality, "Backstage Pass quality increases even more when concert is almost here");
        }
    
        [Test]
        public void BackstagePass_QualityIsCappedAt50() {
            GildedRose sut = new GildedRose(createItemList(BACKSTAGE_PASS, 40, 50));
            sut.UpdateQuality();
            Assert.AreEqual(50, sut.Items[0].Quality, "Quality has an upper limit that is not exceeded");
        }
    
        [Test]
        public void BackStagePass_QualityDropsToZeroWhenConcertPasses() {
            GildedRose sut = new GildedRose(createItemList(BACKSTAGE_PASS, 0, 50));
            sut.UpdateQuality();
            Assert.AreEqual(0, sut.Items[0].Quality, "Backstage Pass is worthless when concert has passed");
        }

        //NEW BEHAVIOR
        // conjured items
    
    }
}
