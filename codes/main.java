// Main.java
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        person.sayHello();
    }
}

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void sayHello() {
        System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");
    }
}
