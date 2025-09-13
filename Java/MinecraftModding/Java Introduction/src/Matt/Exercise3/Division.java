package Matt.Exercise3;

public class Division extends Operation implements IOperation {
    public Division(float a, float b) {
        super(a, b);
    }

    @Override
    public float calculate() {
        //Protection for divide by 0
        if (b != 0) {
            return a / b;
        }
        else {
            return 0;
        }
    }
}
