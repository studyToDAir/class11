package webservice_07;

import java.util.ArrayList;
import java.util.List;

public class TotalExam {

	public static void main(String[] args) {
		// DAO
		List<Integer> list = new ArrayList<Integer>();
		list.add(1111);
		list.add(2222);
		list.add(3333);
		list.add(4444);
		list.add(5555);
		
		// Service
		List<Integer> result = new ArrayList<Integer>();
		for(int i=0; i<list.size(); i++ ) {
			if( (int)list.get(i) > 3000) {
				result.add(list.get(i));
			}
		}
		
		// Jsp
		StringBuffer sb = new StringBuffer();
		
		for( int empno : result ) {
			sb.append("<div>"+ empno +"</div>\n");
		}
		
		String html = sb.toString();
		
		// ServletExam
		System.out.println(html);
		
	}

}
