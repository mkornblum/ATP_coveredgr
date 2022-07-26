package gildedrose;

import static org.junit.Assert.*;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class StepDefinitions {
    private Item[] items = new Item[1];
    private GildedRose app;

    @Given("The item as {string}")
    public void initial_sellin_is_and_quality_is(String name) {
        items[0] = new Item(name, 0, 0);
        app = new GildedRose(items);
    }

    @Given("The item has Sellin of {int}")
    public void the_item_has_sellin_of(Integer sellin) {
        items[0].sellIn = sellin;
    }

    @Given("the item has Quality of {int}")
    public void the_item_has_quality_of(Integer quality) {
        items[0].quality = quality;
    }

    @When("I update the quality")
    public void i_update_the_quality() {
        app.updateQuality();
    }

    @Then("I should get item as {string}")
    public void i_should_get_sellin_as_and_quality_as(String expected) {
        assertEquals(expected, app.items[0].name);
    }

    @Then("I should get item with Quality of {int}")
    public void i_should_get_item_with_quality_of(Integer expected) {
        assertEquals(expected.intValue(), app.items[0].quality);
    }
}

