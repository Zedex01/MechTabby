package Matt;

public abstract class Animal {
    //Fields/attributes
    public String picture;
    protected String name;
    private int age;

    //Constructor
    public Animal(String picture, String name, int age) {
        this.picture = picture;
        this.name = name;
        this.age = age;
    }

    public abstract void move();

    public void makeSound() {
        System.out.println("Whatever Animal Sound");
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age + " years");
        System.out.println("Picture: " + picture);
    }

    public int getAge() {
        return age;
    }

    public void birthday() {
        age++;
        System.out.println(name + " is celebrating their birthday! they are now " + age);
    }
}
