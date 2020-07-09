package gildedrose;

import org.approvaltests.Approvals;
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
}
