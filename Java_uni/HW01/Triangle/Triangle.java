public class Triangle {

    public double first_side;
    public double second_side;
    public double third_side;
    public double radians;
    public double area;

    public Triangle(double first_side, double second_side, double radians) {
        this.first_side = first_side;
        this.second_side = second_side;
        this.radians = Math.toRadians(radians);
    }

    public double getThirdside() {
        return this.third_side;
    }

    public double getArea() {
        return this.area;
    }

    public void ThirdsideCalculate() {
        // 餘弦公式: c^2 = a^2 + b^2 - 2abcosθ
        this.third_side = Math.sqrt(
                Math.pow(this.first_side, 2) +
                        Math.pow(this.second_side, 2) -
                        2 * this.first_side * this.second_side * Math.cos(this.radians));
    }

    public void AreaCalculate() {
        // 海龍公式: s = (a+b+c)/2, 面積=sqrt(s * (s-a) * (s-b) * (s-c))
        double s = (this.first_side + this.second_side + this.third_side) / 2;
        this.area = Math.sqrt(s * (s - this.first_side) * (s - this.second_side) * (s - this.third_side));
    }

}
