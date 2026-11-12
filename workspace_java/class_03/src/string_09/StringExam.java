package string_09;

public class StringExam {

	public static void main(String[] args) {

		String s = "영일이삼사오육칠팔구삼사";
		
		char c = s.charAt(3);
		System.out.println(c);
		
		System.out.println(s.length());
		
		int i = s.indexOf("삼사");
		System.out.println(i);
		
		int i2 = s.lastIndexOf("삼사");
		System.out.println(i2);
		
		// indexOf를 사용하지 않고 구현하시오.
		String email = "todair@naver.com";
		// [@]하나, [.]하나 이상 있으면 "이메일 맞음" 하나라도 없으면 "이메일 아님"
		if(email.indexOf("@") != -1 && email.indexOf(".") != -1) {
			System.out.println("이메일 맞음");
		} else {
			System.out.println("이메일 아님");
		}
		
		int cnt_골뱅이 = -1;
		int cnt_쩜 = -1;
		for(int j=0; j<email.length(); j++) {
			if(email.charAt(j) == '@') {
				cnt_골뱅이 = j;
			} else if (email.charAt(j) == '.') {
				cnt_쩜 = j;
			}
		}
		
		if(cnt_골뱅이 != -1 && cnt_쩜 != -1) {
			System.out.println("이메일 맞음:"+cnt_골뱅이+", "+cnt_쩜);	
		} else {
			System.out.println("이메일 아님");
		}
		
		
		String s2 = s.replace("삼사", "34");
		System.out.println(s);
		System.out.println(s2);
		
		s2 = s.substring(5, 8);
		System.out.println(s2);
		
		s2 = s.substring(5);
		System.out.println(s2);
		
		String[] s3 = s.split("삼");
		for(String a : s3) {
			System.out.println(a);
		}
		
		double r = Math.random();
		System.out.println(r);
	}

}







