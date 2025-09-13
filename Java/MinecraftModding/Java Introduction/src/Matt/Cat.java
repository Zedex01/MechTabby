package Matt;

public class Cat extends Animal {
    public Cat(String picture, String name, int age) {
        super(picture, name, age);
    }

    @Override
    public void move() {
        System.out.println("Cat is sneaking!");
    }

    //Overrides the method from one of it is super classes
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }


}
