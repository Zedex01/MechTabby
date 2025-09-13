package Matt.Exercise3;

public class Multiplication extends Operation implements IOperation{


    public Multiplication(float a, float b) {
        super(a, b);
    }

    @Override
    public float calculate() {
        return a * b;
    }
}
