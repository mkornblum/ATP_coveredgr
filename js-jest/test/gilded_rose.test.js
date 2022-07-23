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

  it.each([
    ["generic item"],
    ["Aged Brie"],
    ["Backstage passes to a TAFKAL80ETC concert"],
  ])('%p item  SellIn will be negative after sellIn date reached', (itemName) => {
    const sut = new Shop([new Item(itemName, 0, 25)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(-1);
  });

  it("Generic item quality decreases by 1 before sellIn date reached", () => {
    const sut = new Shop([new Item("generic item", 5, 10)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(9);
  });

  it("Generic item quality decreases twice as fast after sellIn date reached", () => {
    const sut = new Shop([new Item("generic item", 0, 10)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(8);
  });

  it("Generic item quality never decreases below 0", () => {
    const sut = new Shop([new Item("generic item", 5, 0)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(0);
  });

  it("Aged Brie quality improves with age", () => {
    const sut = new Shop([new Item("Aged Brie", 5, 30)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(31);
  });

});
