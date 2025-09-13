package Matt.Exercise3;

public abstract class Operation {
    public float a;
    public float b;

    //Constructor
    public Operation(float a, float b){
        this.a = a;
        this.b = b;
    }

    public void Display(){
        System.out.println("a is " + a + " | b is " + b);
    }
}
