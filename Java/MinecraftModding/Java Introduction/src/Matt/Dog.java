package Matt;

//Classes start with upper case
public class Dog extends Animal{
    public Dog(String picture, String name, int age) {
        super(picture, name, age);
    }

    @Override
    public void move() {
        System.out.println("Dog is runnnig");
    }

    //Overrides the method from one of it is super classes
    @Override
    public void makeSound() {
        System.out.println("Woof");
    }
}
