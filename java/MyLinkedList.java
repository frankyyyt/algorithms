
/**
 * Created by ehrlichja on 1/20/14.
 */
public class MyLinkedList {

    private Node head = new Node();

    private class Node {
        String value = "default_value";
        Node next = null;
    }

    public void push(String value) {
        Node oldhead = head;
        head = new Node();
        head.value = value;
        head.next = oldhead;
    }

    public Node pop() {
        Node newhead = head.next;
        Node popped = head;
        head = newhead;
        return popped;
    }

    public void search(String query, Node node) {
        if (node.value == query) {
            System.out.println("found it");
        } else if (node.next != null) {
            search(query, node.next);
        };

    }

    public void count() {
        Node node = head;
        int count = 1;
        while (node.next != null) {
            count++;
            node = node.next;
        }
        System.out.println("There are " + Integer.toString(count) + " nodes in the list");
    }

    public static void main(String[] args) {

        Stopwatch smallLLtimer = new Stopwatch();
        MyLinkedList smallLL = new MyLinkedList();
        int small = 10000;
        for (int i = 1; i < small; i++) {
            smallLL.push(Integer.toString(i));
        }
        smallLL.count();
        System.out.println(smallLLtimer.elapsedTime());


        Stopwatch bigLLtimer = new Stopwatch();
        MyLinkedList bigLL = new MyLinkedList();
        int big = 10000000;
        for (int i = 1; i < big; i++) {
            bigLL.push(Integer.toString(i));
        }
        bigLL.count();
        System.out.println(bigLLtimer.elapsedTime());

        System.out.println(bigLL.pop().value);
        bigLL.count();
        System.out.println(bigLL.pop().value);
        bigLL.count();

    }

}
