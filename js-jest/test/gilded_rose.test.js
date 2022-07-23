const {Shop, Item} = require("../src/gilded_rose");

describe("Gilded Rose", function() {
  it("Legendary Item quality does not decrease", () => {
    // Arrange
    const sut = new Shop([new Item("Sulfuras, Hand of Ragnaros", 20, 80)]);

    // Act
    const items = sut.updateQuality();

    // Assert
    expect(items[0].quality).toBe(80);
  });

  it("Legendary Item never has to be sold", () => {
    const sut = new Shop([new Item("Sulfuras, Hand of Ragnaros", 1, 80)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(1);
  });

  it("Legendary Item quality does not change after sellin", () => {
    const sut = new Shop([new Item("Sulfuras, Hand of Ragnaros", -1, 80)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(80);
  });

  it.each([
    ["generic item"],
    ["Aged Brie"],
    ["Backstage passes to a TAFKAL80ETC concert"],
  ])('%p item SellIn decreases each update', (itemName) => {
    const sut = new Shop([new Item(itemName, 8, 10)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(7);
  });



});
