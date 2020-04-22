use base64;
use hex;

pub fn hex_to_base64(input: &String) -> String {
    base64::encode(hex::decode(input).unwrap())
}