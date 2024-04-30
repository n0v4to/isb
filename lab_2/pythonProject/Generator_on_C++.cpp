#include <iostream>
#include <random>
#include <bitset>

/*!
\brief Generates a random binary sequence and prints it to the console.
*/
void generateRandomBinarySequenceCpp() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, 1);

    for (int i = 0; i < 16; ++i) {
        unsigned char byte = 0;
        for (int j = 0; j < 8; ++j) {
            byte = (byte << 1) | dis(gen);
        }
        std::bitset<8> binaryByte(byte);
        std::cout << binaryByte;
    }
}

/*!
\brief The main function that generates a random binary sequence.
\return The exit status of the program
*/
int main() {
    generateRandomBinarySequenceCpp();
    return 0;
}