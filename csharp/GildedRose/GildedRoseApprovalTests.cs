using System.Collections.Generic;
using ApprovalTests;
using ApprovalTests.Reporters;
using NUnit.Framework;

namespace csharp {
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
    }
}