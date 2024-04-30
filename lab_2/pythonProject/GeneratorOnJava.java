import java.security.SecureRandom;

/**
* This class generates a random binary sequence of length 128.
*/
public class GeneratorOnJava {
    /**
     * The main method that triggers the generation of the sequence.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        GeneratorOnJava generator = new GeneratorOnJava();
        byte[] byteArray = new byte[16];

        generator.nextBytes(byteArray);

        for (byte b : byteArray) {
            String binaryString = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            System.out.print(binaryString);
        }
    }

    /**
     * Method for generating pseudo-random bytes into an array.
     *
     * @param bytes The byte array where the generated values will be stored.
     */
    public void nextBytes(byte[] bytes) {
        SecureRandom secureRandom = new SecureRandom();
        secureRandom.nextBytes(bytes);
    }
}
