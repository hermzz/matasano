pub fn xor(input: &Vec<u8>, xor: &Vec<u8>) -> Vec<u8> {
    let mut result: Vec<u8> = Vec::new();

    let mut pos = 0;
    while pos < input.len() {
        result.push(input[pos] ^ xor[pos % xor.len()]);

        pos += 1;
    }

    result
}