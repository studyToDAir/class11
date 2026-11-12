package game_04;

public class Auto {

	void run(Champ champ) {
		champ.attack();
		champ.move();
		champ.skill("F");
		champ.skill("R");
		champ.recall();
		
		if(champ instanceof VI) {
			VI vi = (VI)champ;
			vi.Â¡Å©½º¶û³î±â();
		}
		String a = "a";
		a.equals("b");
	}

}
