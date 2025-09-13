package Matt.Exercise3;

public class Modulus extends Operation implements IOperation{
    public Modulus(float a, float b) {
        super(a, b);
    }

    @Override
    public float calculate() {
        //Protection for divide by 0
        if (b != 0) {
            return a % b;
        }
        else {
            return 0;
        }
    }
}
