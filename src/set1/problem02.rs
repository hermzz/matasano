use crate::common::challenge;
use crate::common::bytes;
use hex;

pub static INFO: challenge::INFO = challenge::INFO {
    no:         2,
    title:      "Fixed XOR",
    help:       "",
    execute_fn: interactive
};

fn xor(input: String, mask: String) -> Result<String, &'static str> {
    let input = match hex::decode(input) {
        Ok(res) => res,
        Err(_) => return Err("Cannot decode input")
    };

    let mask = match hex::decode(mask) {
        Ok(res) => res,
        Err(_) => return Err("Cannot decode mask")
    };

    Ok(hex::encode(bytes::xor(&input, &mask)))
}

pub fn interactive() -> i32 {
    let input = String::from("1c0111001f010100061a024b53535009181c");
    let mask = String::from("686974207468652062756c6c277320657965");

    println!("{:?}", 
        match xor(input, mask) {
            Ok(result) => result,
            Err(msg) => String::from(msg),
        }
    );

    exit_ok!()
}

#[test]
fn fixed_xor() {
    let input = String::from("1c0111001f010100061a024b53535009181c");
    let mask = String::from("686974207468652062756c6c277320657965");

    let result = match xor(input, mask) {
        Ok(res) => res,
        Err(msg) => String::from(msg)
    };

    assert!(result == String::from("746865206b696420646f6e277420706c6179"));
}
