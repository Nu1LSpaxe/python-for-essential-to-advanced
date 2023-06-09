package Enum;

public enum Drink {
    BLACK_TEA(1, 20,"紅茶"),
    GREEN_TEA(2, 20,"綠茶"),
    MILK_TEA(3, 25,"奶茶"),
    BUBBLE_TEA(4, 35,"珍珠奶茶");

    private final int id;
    private final int price;
    private final String name;
    /* 建構式 Start (5pt.) */
    private Drink(int id, int price, String name) {
        this.id = id;
        this.price = price;
        this.name = name;
    }

    /* 建構式 End (5pt.) */

    public int getId() {
        return id;
    }

    public String getName(){
        return name;
    }

    public int getPrice(){
        return price;
    }

    public static Drink getDrinkById(int id) {
        for (Drink drink: Drink.values()) {
            if (drink.getId() == id) {
                return drink;
            }
        }
        return null;
    }

}
