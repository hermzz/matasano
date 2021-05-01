use crate::common::base64;
use crate::common::challenge;

pub static INFO: challenge::INFO = challenge::INFO {
    no:         1,
    title:      "Convert hex to base64",
    help:       "",
    execute_fn: interactive
};

fn hex_to_base64(input: &String) -> String {
    match base64::hex_to_base64(&input) {
        Ok(result) => result,
        Err(_) => String::from("encoding error")
    }
}

pub fn interactive() -> i32 {
    let input = String::from("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    
    println!("Encoded input is {}", hex_to_base64(&input));

    exit_ok!()
}
