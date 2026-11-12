package var_02;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Map_09 {

	public static void main(String[] args) {
		HashMap map = new HashMap();
		
		map.put("k1", "v1");
		map.put("k2", 2);
		map.put("k3", false);
		// 같은 key는 없으면 만들고 있으면 덮어쓰기
		map.put("k2", 3);
		
		System.out.println( map.get("k1") );
		
		String s = (String)map.get("k1");
		
		// 없으면 null
		System.out.println( map.get("k100") );
		
		
		Map<String, Integer> map2 = new HashMap<String, Integer>();
//		Map<String, Integer> map2 = new HashMap<>();
		map2.put("k1", 1);
//		map2.put("k2", "1");
		int a = map2.get("k1");
		
		// 멜론 차트 1~3까지를 저장해서 관리할거임
		// 한 곡당 가수명, 제목으로 저장
		// 모든 곡의 정보를 출력까지
		
		List<Map<String, String>> melon = new ArrayList<Map<String, String>>();
		Map<String, String> song = new HashMap<String, String>();
		song.put("제목", "With");
		song.put("가수", "리센트");
		melon.add(song);
		
		song = new HashMap<String, String>();
		song.put("제목", "꿈꾸던 어른이 되었나요");
		song.put("가수", "머무르");
		melon.add(song);
		
//		System.out.println("melon : "+ melon);
		
		for(int i=0; i<melon.size(); i++) {
			Map map3 = melon.get(i);
//			System.out.println("map3 : "+ map3);
			System.out.println("제목: "+ map3.get("제목"));
			System.out.println("가수: "+ map3.get("가수"));
		}
		
		// final
		int x = 10;
		x = 20;
		
		final int y = 20;
//		y = 200;
	}

}










