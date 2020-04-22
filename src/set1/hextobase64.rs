use crate::common::base64;
use crate::common::challenge;

pub static info: challenge::Info = challenge::Info {
    no:         1,
    title:      "Convert hex to base64",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    let input = String::from("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    let encoded = base64::hex_to_base64(&input);
    println!("Encoded input is {}", encoded);
    
    exit_ok!()
}
