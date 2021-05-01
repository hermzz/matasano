use hex::FromHexError;
use base64;
use hex;

pub fn hex_to_base64(input: &String) -> Result<String, FromHexError> {
    match hex::decode(input) {
        Ok(decoded) => Ok(base64::encode(decoded)),
        Err(e) => Err(e)
    }
}

#[test]
fn encode_base64() {
    let input = String::from("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    
    assert!(hex_to_base64(&input) == Ok(String::from("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")));
}

#[test]
fn hex_decode_error() {
    let input = String::from("aa1");
    
    assert_eq!(hex_to_base64(&input), Err(hex::FromHexError::OddLength));
}