import java.util.Scanner;

public class TriangleProblem {
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        // 輸入三角形設定值
        System.out.println("Input the length of the first side of the triangle (cm): ");
        double first_side = scanner.nextDouble();
        System.out.println("Input the length of the second side of the triangle (cm): ");
        double second_side = scanner.nextDouble();
        System.out.println("Input the degrees of the triangle: ");
        double radians = scanner.nextDouble();

        // 建構三角形
        Triangle triangle = new Triangle(first_side, second_side, radians);

        // 計算三角形的第三邊與面積
        triangle.ThirdsideCalculate();
        triangle.AreaCalculate();

        System.out.printf("the length of the third side of the triangle is: %.2f cm\n", triangle.getThirdside());
        System.out.printf("the area of the triangle is: %.2f cm2\n", triangle.getArea());

        scanner.close();
    }
}
