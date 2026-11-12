package class_01;

public class CarExam {

	// 필드 영역
	
	public static void main(String[] args) {
		int a;
		a = 10;
		System.out.println(a);
		
		Car_02 c1 = new Car_02();
		Car_02 c2 = new Car_02();
		
		int ms = c1.maxSpeed;
		int s = c1.speed;
		System.out.println("c1.speed:"+ s);
		
		c1.speed = 400;
		c2.speed = 399;
		
		System.out.println(c1.speed);
		System.out.println(c2.speed);
		
		System.out.println(c1.power);
		c1.powerOn();
		System.out.println(c1.power);
		
		c1.setSpeed(100);
		c1.setSpeed(400);
		System.out.println(c1.speed);
		
		int s1 = c1.getSpeed(1);
		
		c1.plus(1, 2.0);
		
	}

}
