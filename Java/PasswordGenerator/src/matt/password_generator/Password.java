package matt.password_generator;

import java.security.SecureRandom;

public class Password {
    int length;
    boolean hasSymbols;
    boolean hasLetters;
    boolean hasNumbers;
    boolean hasUpperCase;
    String password;
    String charSet;

    //CharacterSets
    private static final String LETTER_SET = "abcdefghijklmnopqrstuvwxyz";
    private static final String NUMERIC_SET = "0123456789";
    private static final String SYMBOL_SET =  "!@#$%^&*()-_+=";
    private static final String UPPER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    //Random Generator
    private static final SecureRandom random = new SecureRandom();

    //Full Constructor
    public Password(int length, boolean hasLetters, boolean hasNumbers, boolean hasSymbols, boolean hasUpperCase){
        this.length = length;
        this.hasLetters = hasLetters;
        this.hasNumbers = hasNumbers;
        this.hasSymbols = hasSymbols;
        this.hasUpperCase = hasUpperCase;
        this.password = null;
    }

    //Simple Constructor
    public Password(int length){
        this(length, true, true, true, true);
    }


    // === Methods ===
    public Password generatePassword() {

        char[] charArray = new char[this.length];
        this.charSet = "";
        //Build character set
        if (hasLetters) {this.charSet = this.charSet.concat(LETTER_SET);}
        if (hasNumbers) {this.charSet = this.charSet.concat(NUMERIC_SET);}
        if (hasSymbols) {this.charSet = this.charSet.concat(SYMBOL_SET);}
        if (hasUpperCase) {this.charSet = this.charSet.concat(UPPER_SET);}

        //For each Char in chaArray
        for (int i = 0; i < this.length; i++){
            //Randomly grab a character from within the charset and store it in charArray
            charArray[i] = charSet.charAt(random.nextInt(charSet.length()));
        }

        this.password = new String(charArray);
        return this;
    }



    // === Getters and Setters ===
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public boolean isHasSymbols() {
        return hasSymbols;
    }

    public void setHasSymbols(boolean hasSymbols) {
        this.hasSymbols = hasSymbols;
    }

    public boolean isHasLetters() {
        return hasLetters;
    }

    public void setHasLetters(boolean hasLetters) {
        this.hasLetters = hasLetters;
    }

    public boolean isHasNumbers() {
        return hasNumbers;
    }

    public void setHasNumbers(boolean hasNumbers) {
        this.hasNumbers = hasNumbers;
    }

    public boolean isHasUpperCase() {
        return hasUpperCase;
    }

    public void setHasUpperCase(boolean hasUpperCase) {
        this.hasUpperCase = hasUpperCase;
    }

    public String getPassword() {
        return password;
    }

    public String getCharSet() {
        return charSet;
    }
}
