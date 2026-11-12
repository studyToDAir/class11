package melon_02;

import java.util.ArrayList;
import java.util.List;

public class Melon {

	// 필드
//	Song[] songs = new Song[0];
	List<Song> songs = new ArrayList<Song>();
	
	// 생성자

	// 메소드
	/**
	 * 목록 보여주기
	 * 메소드명 : showList
	 * 전달인자 : int count 보여줄 개수
	 * 리턴타입 : void
	 * 
	 * songs의 내용 count 만큼 필요한 정보만 출력하기
	 */
	void showList(int count) {
		// 방어코딩
		// songs의 크기보다 count가 큰 경우
		if( count > songs.size() ) {
			count = songs.size();
		}
//		count = (count > songs.size()) ? songs.size() : count;
		
		for(int i=0; i<count; i++) {
			Song song = songs.get(i);
			System.out.println("title: "+ song.title);
			System.out.println("singer: "+ song.singer);
		}
	}
	
	/**
	 * 곡 추가
	 * 받은 Song을 songs에 추가
	 * 단, 제목과 가수가 같으면 추가하지 않는다
	 * 
	 * 메소드명: addSong
	 * 전달인자: Song
	 * 리턴타입: 추가 성공 여부
	 */
	boolean addSong(Song song) {
		boolean result = false;
		
		if(this.songs.size() == 0) {
			songs.add(song);
			result = true;
		} else {
			for(int i=0; i<this.songs.size(); i++) {
//				Song s = (Song)songs.get(i);
				Song s = songs.get(i);
				
				if( !(s.title.equals(song.title) 
						&& s.singer.equals(song.singer))) {
					
					songs.add(song);
					result = true;
				}
			}
		}
		
		return result;
	}
	
	void playAll() {
		for(int i=0; i<this.songs.size(); i++) {
			songs.get(i).play();
		}
	}
}











