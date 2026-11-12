package game_04;

public class LOL_Exam {

	public static void main(String[] args) {

		VI 바이 = new VI();
		바이.move();
		바이.skill("R");

		Jax jax = new Jax();
		jax.move();
		
		Champ champ1 = (Champ)바이;
		Champ champ2 = jax;
		
		champ1.move();
		champ2.move();
		
		Auto auto = new Auto();
		auto.run(바이);
		auto.run(jax);
		
		VI vi2 = (VI)champ1;
		vi2.징크스랑놀기();
	}

}
