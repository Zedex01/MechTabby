package matt.password_generator;

public class Password {
    int length;
    boolean hasSymbols;
    boolean hasLetters;
    boolean hasNumbers;
    boolean hasUpperCase;
    String password;



    String CHARSET;

    //CharacterSets
    private static final String LetterSet = "abcdefghijklmnopqrstuvwxyz";
    private static final String NumericSet = "0123456789";
    private static final String SymbolSet =  "!@#$%^&*()-_+=";
    private static final String UpperSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


    //Full Constructor
    public Password(int length, boolean hasLetters, boolean hasNumbers, boolean hasSymbols, boolean hasUpperCase){
        this.length = length;
        this.hasLetters = hasLetters;
        this.hasNumbers = hasNumbers;
        this.hasSymbols = hasSymbols;
        this.hasUpperCase = hasUpperCase;
    }

    //Simple Constructor
    public Password(int length){
        this(length, true, true, true, true);
    }


    // === Methods ===
    public String generatePassword() {
        char[] charArray = new char[this.length];

        //Build character set
        if (hasLetters) {this.CHARSET = this.CHARSET.concat(LetterSet);}
        if (hasNumbers) {this.CHARSET = this.CHARSET.concat(NumericSet);}
        if (hasSymbols) {this.CHARSET = this.CHARSET.concat(SymbolSet);}
        if (hasUpperCase) {this.CHARSET = this.CHARSET.concat(UpperSet);}

        for (char character : charArray){
            System.out.println("Debug Text");
        }

        System.out.println(CHARSET);

        this.password = new String(charArray);
        return password;
    }

    public String getPassword() {
        return password;
    }

    public String getCHARSET() {
        return CHARSET;
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
}
