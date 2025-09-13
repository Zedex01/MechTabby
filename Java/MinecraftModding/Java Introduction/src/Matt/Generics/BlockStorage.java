package Matt.Generics;

import java.util.ArrayList;
import java.util.List;

//T is unknown or 'Generic'

public class BlockStorage<T extends Block> {
    private List<T> blocks;

    public BlockStorage() {
        this.blocks = new ArrayList<>();

    }

    public void addBlock(T block) {
        blocks.add(block);
        System.out.println("Added " + block + " to the Block Storage");
    }

    public void displayBlocks(){
        System.out.println("Blocks in our storage:");
        for (T block : blocks) {
            System.out.println("- " + block);
        }
    }

}
