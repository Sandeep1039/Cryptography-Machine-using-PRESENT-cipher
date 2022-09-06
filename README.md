# Cryptography-Machine-using-PRESENT-cipher
### Why to use PRESENT cipher ?
Lightweight Block cipher can provide adequate security with low power consumption and gives higher throughput compared to traditional AES, DES and blowfish encryption methods. The hardware requirement for implementing is also higher in traditional cryptographic methods. This demands higher power consumption and less cost effective for small scale usage. Therefore, using lightweight block cipher for authentication in multi-hop networks is efficient.

### PRESENT Algorithm
The present module is a kind of Substitution Permutation (SP) network consisting of 31 rounds with block length being 64 bits supporting key length 80 bit. 
The top module of PRESENT algorithm that comprises of clock, k_load to initiate the process of data encryption, d-load, key input which is 80 bit in size. 
The size of the input fed is din to be 64 bits. 
![image](https://user-images.githubusercontent.com/65500415/188557092-86a27ce0-fe43-4d84-9652-5390c60c416d.png)

The hardware architecture of PRESENT encryption is in figure. It uses 64 bit of inputs, 64 bit of outputs and 80 bit of key i.e. the key size used 80 bit. 
A single 64-bit register stores the state along with key of 80 bit register which service parallel input and multiple bits shift. 
There is need of 16 cycles in order to load the data to processing of data of 64 bits plain text block. This procedure gives the outputs. 

### Block Diagram
![image](https://user-images.githubusercontent.com/65500415/188557390-155e4c62-a488-4dfa-ac1a-9ce555d51231.png)

### MODULES 
**addRoundKey**-Given round key Ki = κ i 63 . . . κi 0 for 1 ≤ i ≤ 32 and current state b63 . . . b0, addRoundKey consists of the operation for 0 ≤ j ≤ 63, 

**sBoxlayer**-The S-box used in the present is a 4-bit to 4-bit S-box S : F^ 4 → F^ 4 . The action of this box in hexadecimal notation is given by the following table. 

![image](https://user-images.githubusercontent.com/65500415/188557954-9db3a81f-e401-4a46-81cf-5b200a25afc1.png)

For sBoxLayer the current state b63 . . . b0 is considered as sixteen 4-bit words w15 . . . w0 where wi = b4∗i+3||b4∗i+2||b4∗i+1||b4∗i for 0 ≤ i ≤ 15 and the output nibble S[wi ] provides the updated state values in the obvious way. 

**pLayer**- The bit permutation used in present is given by the following table. Bit i of state is moved to bit position P(i).
![image](https://user-images.githubusercontent.com/65500415/188558666-078a977f-5b23-4edc-97b4-a8933f9eee9b.png)

The key schedule. present can take keys of either 80 or 128 bits. However we focus on the version with 80-bit keys. The user-supplied key is stored in a key register K and represented as k79k78 . . . k0. At round i the 64-bit round key Ki = κ63κ62 . . . κ0 consists of the 64 leftmost bits of the current contents of register K. Thus at round i we have that: Ki = κ63κ62 . . . κ0 = k79k78 . . . k16. After extracting the round key Ki , the key register K = k79k78 . . . k0 is updated as follows
![image](https://user-images.githubusercontent.com/65500415/188560332-29f5af9f-3982-4182-b27d-694597807696.png)


### Simulations
![image](https://user-images.githubusercontent.com/65500415/188560127-6dac4e8f-4a90-4816-b783-17ec4d66f7ac.png)






