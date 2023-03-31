class Item {
  constructor(name, sellIn, quality){
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }
}

class UpdateableItem extends Item {
  constructor(name, sellIn, quality, updateCallback) {
    super(name, sellIn, quality);
    this.updateCallback = updateCallback;
  }

  updateQuality() {
    return this.updateCallback(this)
  }
}

const itemUpdateMethods = {
  'Sulfuras, Hand of Ragnaros': () => {},
  'Aged Brie': (item) => {
    item.sellIn = item.sellIn - 1;

    if (item.quality < 50) {
      item.quality = item.quality + (item.sellIn < 0 ? 2 : 1)
    }
    return item
  },
  'Backstage passes to a TAFKAL80ETC concert': (item) => {
    item.sellIn = item.sellIn - 1;
    if (item.sellIn < 0) {
      item.quality = 0;
    } else if (item.sellIn < 5) {
      item.quality = item.quality + 3;
    } else if (item.sellIn < 10) {
      item.quality = item.quality + 2;
    } else if (item.sellIn > 0) {
      item.quality = item.quality + 1;
    }
    item.quality = Math.min(50, item.quality)
    return item
  }
}

const genericUpdateMethod = (item) => {
  item.sellIn = item.sellIn - 1;

  if (item.quality > 0) {
    item.quality = item.quality - ( item.sellIn > 0 ? 1 : 2);
  }
  return item
}

class Shop {
  constructor(items=[]){
    this.items = items.map((item) => {
      let method = itemUpdateMethods[item.name] || genericUpdateMethod
      return new UpdateableItem(item.name, item.sellIn, item.quality, method);
    })
  }

  updateQuality() {
    this.items.forEach((item) => item.updateQuality());
    return this.items;
  }

  // updateQuality() {
  //   for (let i = 0; i < this.items.length; i++) {
  //     if (this.items[i].name != 'Aged Brie' && this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
  //       if (this.items[i].quality > 0) {
  //         if (this.items[i].name != 'Sulfuras, Hand of Ragnaros') {
  //           this.items[i].quality = this.items[i].quality - 1;
  //         }
  //       }
  //     } else {
  //       if (this.items[i].quality < 50) {
  //         this.items[i].quality = this.items[i].quality + 1;
  //         if (this.items[i].name == 'Backstage passes to a TAFKAL80ETC concert') {
  //           if (this.items[i].sellIn < 11) {
  //             if (this.items[i].quality < 50) {
  //               this.items[i].quality = this.items[i].quality + 1;
  //             }
  //           }
  //           if (this.items[i].sellIn < 6) {
  //             if (this.items[i].quality < 50) {
  //               this.items[i].quality = this.items[i].quality + 1;
  //             }
  //           }
  //         }
  //       }
  //     }
  //     if (this.items[i].name != 'Sulfuras, Hand of Ragnaros') {
  //       this.items[i].sellIn = this.items[i].sellIn - 1;
  //     }
  //     if (this.items[i].sellIn < 0) {
  //       if (this.items[i].name != 'Aged Brie') {
  //         if (this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
  //           if (this.items[i].quality > 0) {
  //             if (this.items[i].name != 'Sulfuras, Hand of Ragnaros') {
  //               this.items[i].quality = this.items[i].quality - 1;
  //             }
  //           }
  //         } else {
  //           this.items[i].quality = this.items[i].quality - this.items[i].quality;
  //         }
  //       } else {
  //         if (this.items[i].quality < 50) {
  //           this.items[i].quality = this.items[i].quality + 1;
  //         }
  //       }
  //     }
  //   }

  //   return this.items;
  // }
}

module.exports = {
  Item,
  Shop
}
