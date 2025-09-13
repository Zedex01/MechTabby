package Matt.Enums;

//Advanced Enum
public enum ToolMaterial {
    WOOD("wood", 1, 0.3f),
    STONE("stone", 4, 1.5f),
    IRON("iron", 8, 3f);

    private String displayName;
    private int durability;
    private float miningSpeed;

    //Can only be used within this advanced enum, no need for public etc...
    ToolMaterial(String name, int durability, float miningSpeed){
        this.displayName = name;
        this.durability = durability;
        this.miningSpeed = miningSpeed;
    }

    public String getDisplayName() {
        return displayName;
    }

    public int getDurability() {
        return durability;
    }

    public float getMiningSpeed() {
        return miningSpeed;
    }
}
