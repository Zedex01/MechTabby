package Matt.Exercise3;

public class Subtraction extends Operation implements IOperation  {

    public Subtraction(float a, float b) {
        super(a, b);
    }

    @Override
    public float calculate() {
        return a - b;
    }
}
