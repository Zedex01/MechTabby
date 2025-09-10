package matt;

import matt.password_generator.Password;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        final int COUNT = 20;

        //Create a list for the passwords
        List<Password> PASSWORDS =  new ArrayList<>();

        //create n different passwords and store them in the list.
        for (int i = 0; i < COUNT; i++){
            PASSWORDS.add((new Password(12).generatePassword()));
        }

        //Print out all the saved passwords
        for (Password pass: PASSWORDS){
            System.out.printf("%s\n", pass.getPassword());
        }
    }
}