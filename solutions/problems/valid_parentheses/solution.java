class Solution {
    public boolean isValid(String s) {

        CharStackWithArray checker = new CharStackWithArray(s.length());
        if (s.length() == 1) {
            return false;
        }
        while (s.length() != 0) {
            // get element and remove it from string
            String element = s.substring(0, 1);
            s = s.substring(1);

            //check for the symbol
            if (element.equals("(") || element.equals("[") || element.equals("{")) {
                //open symbols goes to the stack to check
                checker.push(element.charAt(0));
            } else {
                //closes symbols check the last inserted open
                if (checker.getSize() <= 0) {
                    // return false if it starts with close symbol
                    return false;
                }
                char check = checker.pop();

                if (String.valueOf(check).equals("(")) {
                    if (!element.equals(")")) {
                        return false;
                    }
                }
                if (String.valueOf(check).equals("[")) {
                    if (!element.equals("]")) {
                        return false;
                    }
                }
                if (String.valueOf(check).equals("{")) {
                    if (!element.equals("}")) {
                        return false;
                    }
                }            
            }

        }
        if (checker.getSize() == 0) {
            //checked all elements

            return true;
        }
        return false;
    }
}

//copied from https://www.baeldung.com/java-char-stack
public class CharStackWithArray {

    private char[] elements;
    private int size;

    public CharStackWithArray(int size) {
        elements = new char[size];
    }

    public void push(char item) {
        ensureCapacity(size + 1);
        elements[size] = item;
        size++;
    }
    private void ensureCapacity(int newSize) {
        char newBiggerArray[];
        if (elements.length < newSize) {
            newBiggerArray = new char[elements.length * 2];
            System.arraycopy(elements, 0, newBiggerArray, 0, size);
            elements = newBiggerArray;
        }
    }

    public char pop() {
        if (size != 0) {
            return elements[--size];
        }
        char ch = ' ';
        return ch;
    }

    public int getSize() {
        return size;
    }
}


