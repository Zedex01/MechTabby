package Matt.Exercise3;

public class Addition extends Operation implements IOperation{

    public Addition(float a, float b) {
        super(a, b);
    }

    @Override
    public float calculate() {
        return a + b;
    }
}
