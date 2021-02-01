using System;
using System.Collections.Generic;
using ApprovalTests;
using ApprovalTests.Combinations;
using ApprovalTests.Reporters;
using NUnit.Framework;

namespace GildedRose {
    
    [UseReporter(typeof(DiffReporter))]
    [TestFixture]
    public class GildedRoseApprovalTests {

        private List<Item> createItemList(string itemName, int sellIn, int quality) {
            return new List<Item> { new Item { Name = itemName, SellIn = sellIn, Quality = quality } };
        }  
        
        [Test]
        public void OneItemApproval() {
            // Arrange
            GildedRose sut = new GildedRose(createItemList("Sulfuras, Hand of Ragnaros", 20, 80));
    
            // Act
            sut.UpdateQuality();
    
            // Assert
            // The Verify call creates a file named GildedRoseApprovalTests.OneItemApproval.received.txt
            // and compares it against the Approved result file, GildedRoseApprovalTests.OneItemApproval.approved.txt
            // If the contents of the two files match, the test passes
            // otherwise the test fails and the diff of the two files is shown
            Approvals.Verify(sut.Items[0].ToString());
        }

        [Test]
        public void AllItemCombinations() {
            CombinationApprovals.VerifyAllCombinations(
                DoUpdateQuality,
                new string[] {"foo", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"},
                new int[] {-1, 0, 5, 10, 11},       // SellIn
                new int[] { 0, 1, 49, 50 }          // Quality
                );
        }
        
        private string DoUpdateQuality(string name, int sellIn, int quality) {
            var items = createItemList(name, sellIn, quality);
            GildedRose sut = new GildedRose(items);
            sut.UpdateQuality();
            return sut.Items[0].ToString();
        }
    }
}