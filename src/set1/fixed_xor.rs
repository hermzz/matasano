use crate::common::challenge;
use crate::common::xor;
use hex;


pub static INFO: challenge::INFO = challenge::INFO {
    no:         2,
    title:      "Fixed XOR",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    let input = match hex::decode(String::from("1c0111001f010100061a024b53535009181c")) {
        Ok(res) => res,
        Err(_error) => return exit_err!()
    };

    let xor = match hex::decode(String::from("686974207468652062756c6c277320657965")) {
        Ok(res) => res,
        Err(_error) => return exit_err!()
    };

    println!("{:?}", hex::encode(xor::xor(&input, &xor)));

    exit_ok!()
}
