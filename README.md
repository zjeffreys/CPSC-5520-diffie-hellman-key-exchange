# CPSC-5520-diffie-hellman-key-exchange

Diffie Hellman Extra credit lab – key exchange
Use Python to implement the Diffie Hellman key exchange between two nodes. Each node should generate a random number at the beginning of the program to be used as x and y in the algorithm. The first node, Node Bob, should be created and wait for a response from another node. The second node, node Alice, should be started with the address to the first node. When the second node , node Alice, begins it should send a message to Node (Bob) with (n, g, and g^x mod n). After receiving a message from the Alice, node 1 (Node Bob) should receive the message and raise the value of the key to the power of y, the random variable established at the beginning of the node. Node Bob w ill store this value for future communication. Following storing the symmetrical key, Node (Bob) should calculate g^y mod n and send it back to Node Alice. After receiving the response message back from Node Bob, Node Alice should multiple the g^y mod n by its x to obtain the shared key between Alice and Bob.
After receiving the message both nodes should print out the values of their new symmetrical key and print it to console to show how both nodes have the same shared key after the key exchange.
Requirements:
• Node Alice should communicate with Node Bob with the message n, g, g^x mod n.
• Node Bob should compute the shared key by raising it to the power of y.
• Node Bob should send a message containing g^y mod n back to Node Alice
• Node Alice should compute the shared key by raising it to the power of x
• Both Alice and Bob should print out the same number after they communicate
• Should use TCP/IP to stream messages back and forth.
