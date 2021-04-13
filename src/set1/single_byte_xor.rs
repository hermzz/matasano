use crate::common::challenge;
use crate::common::xor;

pub static INFO: challenge::INFO = challenge::INFO {
    no:         3,
    title:      "Single byte XOR",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    let input = match hex::decode(String::from("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")) {
        Ok(res) => res,
        Err(_error) => return exit_err!()
    };

    match xor::find_best_xor_match(&input) {
        Some(best_match) => println!("Best match was {:?}", best_match),
        None => println!("Nothing found")
    }

    exit_ok!()
}
