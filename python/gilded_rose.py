# -*- coding: utf-8 -*-

# To-Dos
# Where to put the update quality func
# What kinds of tests?

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update each item's quality."""
        for item in self.items:
            item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    

# Special item classes 
class AgedBrie(Item):
    """Increases in quality as it ages."""

    def update(self):
        print(f"Before update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1

        print(f"After update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")


class BackstagePass(Item):
    """Increases in quality as the concert approaches."""

    def update(self):
        print(f"Before update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in > 10:
            self.quality += 1
        elif (self.sell_in <= 10) and (self.sell_in > 5):
            self.quality += 2
        elif self.sell_in <= 5:
            self.quality += 3

        print(f"After update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

# Prob don't even need this.
class Sulfuras(Item):
    """Legendary item - does not decrease in quality or sell_in."""
    def update(self):
        self.sell_in -= 1
        self.quality = self.quality


class Conjured(Item):
    """Degrades in quality twice as fast."""
    
    def update(self):
        print(f"Before update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

        self.sell_in -= 1
        if self.quality > 0:
            self.quality -= 2
            if self.sell_in < 0:
                self.quality -= 4

        print(f"After update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

class NormieItem(Item):
    """Handle the behavior of normie items."""

    def update(self):
        print(f"Before update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

        self.sell_in -= 1
        if (self.sell_in < 0) and (self.quality > 1):
            self.quality -= 2
        elif(self.quality > 0):
            self.quality -= 1

        print(f"After update: {self.name} | Sell In: {self.sell_in} | Quality: {self.quality}")

    """
    def update(self):
        for item in self.items:

            # Maintains the quality of items that cannot decrease in value.
            if item.name not in [self.brie, self.stage_pass, self.sulfuras] and item.quality > 0:
                item.quality -= 1


            # Adds to the quality of special items. Stage pass increases more in value 
            # as the concert approaches. 
            else:   
                item.quality = item.quality + 1
                if item.name == self.stage_pass:
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                    if item.sell_in < 6:
                        item.quality = item.quality + 1

            # Counts down to sell date. Sulfuras does not need to be sold. 
            if item.name != self.sulfuras:
                item.sell_in = item.sell_in - 1

            # Decreases the value of normal items
            if item.sell_in < 0:
                if item.name not in [self.brie, self.stage_pass] and item.quality > 0:
                    if item.name != self.sulfuras:
                        item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    item.quality = item.quality + 1

            if item.quality > 50:
                item.quality = 50
    """

