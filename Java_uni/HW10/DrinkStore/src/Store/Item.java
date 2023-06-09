package Store;
import Enum.*;
public class Item {
    private Drink drink;
    private int quantity;
    private Ice ice;
    private Sugar sugar;

    public Item(Drink drink, int quantity, Ice ice, Sugar sugar) {
        this.drink = drink;
        this.quantity = quantity;
        this.ice = ice;
        this.sugar = sugar;
    }

    public Item() { }

    public void setDrink(Drink drink) {
        this.drink = drink;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void setIce(Ice ice) {
        this.ice = ice;
    }

    public void setSugar(Sugar sugar) {
        this.sugar = sugar;
    }

    // Get drink name
    public String getName() {
        return this.drink.getName() /*  取得品名 */;
    }
    // Get drink amount
    public int getQuantity() {
        return this.quantity;
    }
    // Get drink price
    public int getPrice() {
        return this.drink.getPrice() /*  取得此品項的單價 */;
    }
    // Get drink total price (price * amount)
    public int getTotalPrice() {
        return this.getPrice() * this.getQuantity() /*  取得此品項的總價 */;
    }
    // Get drink ice
    public Ice getIce() {
        return this.ice;
    }
    // Get drink sugar
    public Sugar getSugar() {
        return this.sugar;
    }
    // Show item info
    @Override
    public String toString() {
        return String.format(
                "%-8s\t%-3s\t\t%-3s\t\t%3s\t\t$%6s\t\t$%6s\n",
                this.getName(), this.ice.getDescription(), this.sugar.getDescription(), this.quantity, 
                this.getPrice(), this.getTotalPrice());
    }
}
