import java.util.ArrayList;

/**
 * Created by ehrlichja on 1/21/14.
 */
public class ResizingArrayDeque {

    public static class Item {
        String value;
    }

    private ArrayList<Item> theList = new ArrayList();

    private int size = 0;
    private Item leftmost = null;
    private Item rightmost = null;

    public boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }

    public int size() {
        return size;
    }

    public void pushLeft(Item item) {
        size++;
        theList.add(item);
    }

    public void pushRight(Item item) {
        size++;
        theList.add(0, item);
    }

    public Item popLeft() {
        size--;
        Item popped = theList.remove(0);
        return popped;
    }

    public Item popRight() {
        size--;
        Item popped = theList.remove(theList.size());
        return popped;
    }

    public static void main(String[] args) {

        ResizingArrayDeque testDeque = new ResizingArrayDeque();
        if (testDeque.isEmpty() != true) throw new AssertionError();

        if (testDeque.size() != 0) throw new AssertionError();

        Item newItem = new Item();
        newItem.value = "1st item";
        testDeque.pushLeft(newItem);

        if (testDeque.isEmpty() != false) throw new AssertionError();
        if (testDeque.size() != 1) throw new AssertionError();

        Item anotherNewItem = new Item();
        anotherNewItem.value = "2nd item";
        testDeque.pushRight(anotherNewItem);

        if (testDeque.isEmpty() != false) throw new AssertionError();
        if (testDeque.size() != 2) throw new AssertionError();

        Item poppedLeft = testDeque.popLeft();
        if (testDeque.isEmpty() != false) throw new AssertionError();
        if (testDeque.size() != 1) throw new AssertionError();
        if (poppedLeft.value.equals("1st item") != true) throw new AssertionError();

        Item poppedRight = testDeque.popRight();
        if (testDeque.isEmpty() != true) throw new AssertionError();
        if (testDeque.size() != 0) throw new AssertionError();
        if (poppedRight.value.equals("2nd item") != true) throw new AssertionError();


    }

}
