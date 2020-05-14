use crate::common::challenge;
use crate::common::xor;

pub static info: challenge::Info = challenge::Info {
    no:         2,
    title:      "Fixed XOR",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    let input = String::from("1c0111001f010100061a024b53535009181c");
    let xor = String::from("686974207468652062756c6c277320657965");

    println!("{:?}", match xor::hex(input, xor) {
        Ok(result) => result,
        Err(e) => e.to_string()
    });

    exit_ok!()
}
