package Matt.Exercise3;

public class Calculator {
    //Use Default constructor

    //Field
    private float a;
    private float b;
    private String op;

    //Methods
    public void setA(float a){
        this.a = a;
    }
    public void setB(float b){
        this.b = b;
    }
    public void setOp(String op){
        this.op = op;
    }

    public float[] getAnswer(){
        float[] ans = new float[2];
        ans[0] = 1;
        switch (op){
            case "+":
                Addition add = new Addition(a,b);
                ans[1] = add.calculate();
                break;
            case "-":
                Subtraction sub = new Subtraction(a,b);
                ans[1] = sub.calculate();
                break;
            case "*":
                Multiplication multi = new Multiplication(a,b);
                ans[1] = multi.calculate();
                break;
            case "/":
                Division div = new Division(a,b);
                ans[1] = div.calculate();
                break;
            case "%":
                Modulus mod = new Modulus(a,b);
                ans[1] = mod.calculate();
                break;

            default:
                System.out.println("Invalid Entry");
                ans[0] = -1;
        }

        return ans;
    }
}
